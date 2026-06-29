import json
import os

RULES_PATH = os.path.join(os.path.dirname(__file__), "../rules/prohibited_terms.json")

def load_rules():
    with open(RULES_PATH, "r") as f:
        return json.load(f)

def analyze_text(text: str):
    rules = load_rules()
    findings = []

    text_lower = text.lower()

    for item in rules["managerial_terms"]:
        term = item["term"]

        if term in text_lower:
            findings.append({
                "term": term,
                "severity": item["severity"],
                "reason": item["reason"]
            })

    return findings