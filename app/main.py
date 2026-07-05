from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title = "VisaGuard Compliance Engine", version = "1.0")

class ChatMessage(BaseModel):
    role: str
    content: str

class ChatHistoryRequest(BaseModel):
    history: List[ChatMessage]

class RiskFlag(BaseModel):
    matched_text: str
    reason: str
    suggested_alternative: str

class ChatAnalysisResponse(BaseModel):
    agent_message: str
    risk_score: int
    overall_risk_level: str
    requires_more_info: bool
    flags: List[RiskFlag]

def compute_compliance_telemetry(latest_input: str, high_risk_tokens: list) -> tuple:
    flags = []
    base_score = 0

    for trigger, metadata in high_risk_tokens.items():
        if trigger.lower() in latest_input.lower():
            flags.append(RiskFlag(
                matched_text = trigger,
                reason = metadata["reason"],
                suggested_alternative = metadata["alternative"]
            ))
            base_score += metadata["weight"]

    risk_score = min(100, base_score)
    
    if risk_score >= 75:
        level = "Critical"
    elif risk_score >= 45:
        level = "High"
    elif risk_score >= 20:
        level = "Medium"
    else:
        level = "Safe"
        
    requires_more = len(latest_input.split()) < 15 or risk_score == 0
    
    return risk_score, level, requires_more, flags