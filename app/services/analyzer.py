import json
import os
import re
from typing import List, Dict, Any
from pydantic import BaseModel, Field
from google import genai
from google.genai import types

RULES_PATH = os.path.join(os.path.dirname(__file__), "..", "rules", "prohibited_terms.json")

# Word-form lookup replacing spaCy's lemmatizer — the term list is small and
# fixed, so hardcoding inflections (including irregulars like lead -> led,
# oversee -> oversaw) avoids needing a full NLP pipeline just for this.
_INFLECTIONS = {
    "manage": ["manage", "manages", "managed", "managing"],
    "lead": ["lead", "leads", "led", "leading"],
    "direct": ["direct", "directs", "directed", "directing"],
    "oversee": ["oversee", "oversees", "oversaw", "overseeing", "overseen"],
}
_SURFACE_TO_LEMMA = {form: lemma for lemma, forms in _INFLECTIONS.items() for form in forms}
_WORD_PATTERN = re.compile(r"[A-Za-z']+")
_SENTENCE_SPLIT = re.compile(r'[.\n!?]+')

class ComplianceFlag(BaseModel):
    matched_text: str
    start: int
    end: int
    severity: str
    reason: str
    suggested_alternative: str

class ConversationTurnResponse(BaseModel):
    agent_message: str = Field(description = "The conversational text response to guide the user or ask clarifying questions.")
    requires_more_info: bool = Field(description = "True if the input is too vague or missing details, forcing a follow-up question. False if clear.")
    risk_score: int = Field(default=0, description = "The compliance risk score (0-100) provided by the local check.")
    overall_risk_level: str = Field(default = "Safe", description = "The risk level rating provided by the local check.")
    flags: List[ComplianceFlag] = Field(default_factory = list, description = "List of granular violations detected in the text.")


def rules_engine(text: str) -> dict:
    with open(RULES_PATH, "r") as f:
        rules = json.load(f)
    findings = []

    severity_weights = {
        "low": 10,
        "medium": 30,
        "high": 70,
        "critical": 100
    }
    accumulated_risk = 0

    term_lookup = {item["term"].lower(): item for item in rules["managerial_terms"]}
    technical_objects = {"pipeline", "pipelines", "system", "systems", "database", "databases", "code"}

    # Tag each character with a sentence index so the following-words window
    # below (approximating spaCy's dependency-child check) never crosses a
    # sentence boundary.
    sentence_id_at = [0] * (len(text) + 1)
    current_id = 0
    for i, ch in enumerate(text):
        sentence_id_at[i] = current_id
        if ch in ".\n!?":
            current_id += 1
    sentence_id_at[len(text)] = current_id

    tokens = list(_WORD_PATTERN.finditer(text))

    for i, match in enumerate(tokens):
        word = match.group(0).lower()
        lemma = _SURFACE_TO_LEMMA.get(word)
        if lemma is None or lemma not in term_lookup:
            continue

        item = term_lookup[lemma]
        severity = item.get("severity", "low").lower()
        weight = severity_weights.get(severity, 10)

        # Approximate spaCy's dependency-child check (was the verb's object a
        # technical noun like "pipeline"/"database"?) by looking at the next
        # few words in the same sentence, since English verb-object order
        # puts the object shortly after the verb.
        token_sentence = sentence_id_at[match.start()]
        following_words = []
        for j in range(i + 1, min(i + 5, len(tokens))):
            if sentence_id_at[tokens[j].start()] != token_sentence:
                break
            following_words.append(tokens[j].group(0).lower())
        is_false_positive = any(obj in following_words for obj in technical_objects)

        if not is_false_positive:
            start, end = match.start(), match.end()
            findings.append({
                "term": lemma,
                "matched_text": text[start:end],
                "start": start,
                "end": end,
                "severity": item["severity"],
                "reason": item["reason"],
                "suggested_alternative": item.get("suggestion", "rephrase phrase structurally")
            })
            accumulated_risk += weight

    final_risk_score = min(accumulated_risk, 100)

    if final_risk_score >= 70:
        overall_risk = "Critical"
    elif final_risk_score >= 40:
        overall_risk = "Medium"
    elif final_risk_score > 0:
        overall_risk = "Low"
    else:
        overall_risk = "Safe"

    return {
        "risk_score": final_risk_score,
        "overall_risk_level": overall_risk,
        "flags": findings
    }