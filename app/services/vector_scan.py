import numpy as np
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from app.config import settings
from app.schemas import RiskFlag

REGULATORY_KB = [
    {
        "category": "Management Consultant",
        "anchor_phrases": [
            "managing day to day operations and staff",
            "execution of corporate business strategy",
            "operating in a daily managerial or executive capacity",
            "directing product lines and project management timelines"
        ],
        "reason": "Explicitly flagged under 8 CFR 214.6. Management consultants must strictly operate in an advisory capacity, not operational management.",
        "alternative": "Reframe responsibilities around 'strategic evaluation' or 'process auditing'.",
        "base_weight": 60
    },
    {
        "category": "Non-Statutory Product Management",
        "anchor_phrases": [
            "owning product roadmap and business market fit",
            "cross functional team leadership and revenue metrics",
            "managing feature prioritization and marketing alignment",
            "product manager responsible for lifecycle execution"
        ],
        "reason": "Product Management is not a recognized statutory profession under the TN classification system.",
        "alternative": "Re-evaluate if duties align with 'Computer Systems Analyst' or 'Engineer'.",
        "base_weight": 85
    },
    {
    "category": "Engineering/Technical Team Management",
    "anchor_phrases": [
        "managed a team of engineers building software",
        "led technical strategy and architecture decisions for a team",
        "oversaw hiring, performance reviews, and staff development",
        "directed sprint planning and engineering resource allocation",
        "led a research or engineering initiative from conception to production",
        "mentored and supervised junior engineers on a team"
    ],
    "reason": "Supervisory management of engineering/technical staff is generally outside the scope of specialty-occupation or TN/H-1B individual-contributor roles.",
    "alternative": "Reframe around individual technical contribution: architecture, implementation, hands-on delivery, rather than people oversight.",
    "base_weight": 65
}
]

class VectorScanService:
    def __init__(self):
        print("Initializing lightweight TF-IDF semantic space...")
        self._bake_knowledge_base()

    def _bake_knowledge_base(self):
        all_anchors = []
        rule_ranges = []
        for rule in REGULATORY_KB:
            start = len(all_anchors)
            all_anchors.extend(rule["anchor_phrases"])
            rule_ranges.append((start, len(all_anchors)))

        # A single vectorizer fit across every rule's anchor phrases, so all anchor
        # vectors and later sentence vectors share the same vocabulary/IDF weights.
        # TfidfVectorizer L2-normalizes rows by default, so a dot product between two
        # rows is already cosine similarity (no separate normalize step needed).
        self.vectorizer = TfidfVectorizer(ngram_range=(1, 2), stop_words="english")
        anchor_matrix = self.vectorizer.fit_transform(all_anchors).toarray().astype(np.float32)

        for rule, (start, end) in zip(REGULATORY_KB, rule_ranges):
            rule["anchor_vectors"] = anchor_matrix[start:end]

    def compute_match_score(self, candidate_profile: str, job_description: str) -> int:
        # Fit a throwaway vectorizer on just this pair so the comparison reflects the
        # actual vocabulary of the resume/JD, rather than the small KB anchor vocabulary.
        vectorizer = TfidfVectorizer(stop_words="english")
        try:
            tfidf = vectorizer.fit_transform([candidate_profile, job_description]).toarray()
        except ValueError:
            return 0
        similarity = float(np.dot(tfidf[0], tfidf[1]))
        # TF-IDF cosine similarities for resume/JD pairs cluster tightly in a low range
        # (~0.0-0.4) compared to embedding-based similarity, so a cube-root scale spreads
        # them out across the 0-100 band far better than a linear one. Calibrated against
        # the 25-resume labeled validation set's expected tiers (see scratch_tune.py).
        scaled = max(0, min(100, int((similarity ** (1 / 3)) * 115)))
        return scaled

    def scan(self, latest_input: str) -> tuple:
        flags = []
        total_risk = 0

        if not latest_input.strip():
            return 0, "Safe", True, []

        sentences = [s.strip() for s in re.split(r'[.\n!]+', latest_input) if s.strip()]
        if not sentences:
            return 0, "Safe", True, []

        sentence_vectors = self.vectorizer.transform(sentences).toarray().astype(np.float32)

        # Vectorized cosine similarity: one matrix multiply per rule (against every
        # anchor phrase at once) instead of a per-sentence/per-anchor Python loop of
        # individual dot-product calls.
        per_rule_best_sim = np.stack([
            (sentence_vectors @ rule["anchor_vectors"].T).max(axis=1)
            for rule in REGULATORY_KB
        ], axis=1)  # shape: (n_sentences, n_rules)

        for s_idx, sentence in enumerate(sentences):
            for r_idx, rule in enumerate(REGULATORY_KB):
                highest_sim = float(per_rule_best_sim[s_idx, r_idx])

                if highest_sim > settings.VECTOR_THRESHOLD:
                    scaled_penalty = int(rule["base_weight"] * highest_sim)
                    total_risk += scaled_penalty
                    flags.append(RiskFlag(
                        matched_text=sentence,
                        reason=f"Matched context via category '{rule['category']}' (Confidence: {highest_sim:.2f}). {rule['reason']}",
                        suggested_alternative=rule["alternative"]
                    ))
                    break

        risk_score = min(100, total_risk)
        level = "Critical" if risk_score >= 75 else "High" if risk_score >= 45 else "Medium" if risk_score >= 20 else "Safe"
        requires_more = len(latest_input.split()) < 15 or risk_score == 0

        return risk_score, level, requires_more, flags

vector_scanner = VectorScanService()