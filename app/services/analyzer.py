import json
import os
import spacy
from typing import List, Dict, Any
from pydantic import BaseModel, Field
from google import genai
from google.genai import types

nlp = spacy.load("en_core_web_sm")

RULES_PATH = os.path.join(os.path.dirname(__file__), "..", "rules", "prohibited_terms.json")

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

    doc = nlp(text)
    text_lower = text.lower()

    severity_weights = {
        "low": 10,
        "medium": 30,
        "high": 70,
        "critical": 100
    }
    accumulated_risk = 0

    for item in rules["managerial_terms"]:
        term = item["term"]
        start = 0
        severity = item.get("severity", "low").lower()
        weight = severity_weights.get(severity, 10)

        while True:
            index = text_lower.find(term, start)

            if index == -1:
                break

            is_false_positive = False

            for token in doc:
                if token.idx <= index < (token.idx + len(token.text)):
                    children_text = [child.text.lower() for child in token.children]

                    technical_objects = ["pipeline", "pipelines", "system", "systems", "database", "databases", "code"]
                    if any(obj in children_text for obj in technical_objects):
                        is_false_positive = True
                    break

            if not is_false_positive:
                findings.append({
                    "term": term,
                    "matched_text": text[index: index + len(term)],
                    "start": index,
                    "end": index + len(term),
                    "severity": item["severity"],
                    "reason": item["reason"],
                    "suggested_alternative": item.get("suggestion", "rephrase phrase structurally")
                })

                accumulated_risk += weight

            start = index + len(term)

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

class ComplianceAgentService:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        self.client = genai.Client(api_key = api_key if api_key else "MOCK_KEY")
        self.model_id = "gemini-2.5-flash"

    def execute_chat_turn(self, conversation_history: List[Dict[str, str]]) -> str:
        """
        Coordinates multi-turn dialogue. Calls the local spaCy tool to grab telemetry,
        then responds to the user while structuring the total state payload.
        """
        system_instruction = (
            "You are an expert U.S. immigration compliance agent evaluating user job profiles.\n"
            "Your objective is to converse with the user and ensure their profile is completely free of managerial violations.\n\n"
            "OPERATING INSTRUCTIONS:\n"
            "1. You have a native tool called 'execute_local_compliance_check'. You MUST call this tool using the user's latest description to gather objective risk data.\n"
            "2. If the user's text is extremely short or vague (e.g., 'I run things'), ask clarifying follow-up questions instead of clearing them. Set requires_more_info = True.\n"
            "3. Synthesize the findings from the tool in your conversational 'agent_message'. Return the final output adhering perfectly to the required JSON schema."
        )