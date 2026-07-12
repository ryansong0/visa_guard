from pydantic import BaseModel, Field
from typing import List, Optional

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

class JobMatchRequest(BaseModel):
    candidate_profile: str
    job_description: str

class OptimizationGap(BaseModel):
    category: str
    detected_risk: str
    optimization_strategy: str

class JobMatchResponse(BaseModel):
    compliance_verdict: str
    overall_match_score: int 
    detected_gaps: List[OptimizationGap]
    optimized_profile: str