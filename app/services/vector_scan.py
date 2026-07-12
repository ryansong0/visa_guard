import numpy as np
import re
from sentence_transformers import SentenceTransformer
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
    }
]

class VectorScanService:
    def __init__(self):
        print(f"Initializing Semantic Space via {settings.EMBEDDING_MODEL}...")
        self.model = SentenceTransformer(settings.EMBEDDING_MODEL)
        self._bake_knowledge_base()

    def _bake_knowledge_base(self):
        for rule in REGULATORY_KB:
            encoded = self.model.encode(rule["anchor_phrases"])
            rule["embeddings"] = [np.array(vec).flatten() for vec in encoded]

    def scan(self, latest_input: str) -> tuple:
        flags = []
        total_risk = 0
        
        if not latest_input.strip():
            return 0, "Safe", True, []
        
        sentences = [s.strip() for s in re.split(r'[.\n!]+', latest_input) if s.strip()]
        if not sentences:
            return 0, "Safe", True, []
        
        sentence_embeddings = self.model.encode(sentences)

        for s_idx, s_embed in enumerate(sentence_embeddings):
            s_vec = s_embed.flatten()
            for rule in REGULATORY_KB:
                highest_sim = -1.0
                for anchor_embed in rule["embeddings"]:
                    norm = np.linalg.norm(s_vec) * np.linalg.norm(anchor_embed)
                    sim = float(np.dot(s_vec, anchor_embed) / norm) if norm != 0 else 0.0
                    if sim > highest_sim:
                        highest_sim = sim

                if highest_sim > settings.VECTOR_THRESHOLD:
                    scaled_penalty = int(rule["base_weight"] * highest_sim)
                    total_risk += scaled_penalty
                    flags.append(RiskFlag(
                        matched_text=sentences[s_idx],
                        reason=f"Matched context via category '{rule['category']}' (Confidence: {highest_sim:.2f}). {rule['reason']}",
                        suggested_alternative=rule["alternative"]
                    ))
                    break

        risk_score = min(100, total_risk)
        level = "Critical" if risk_score >= 75 else "High" if risk_score >= 45 else "Medium" if risk_score >= 20 else "Safe"
        requires_more = len(latest_input.split()) < 15 or risk_score == 0
        
        return risk_score, level, requires_more, flags

vector_scanner = VectorScanService()