from fastapi import FastAPI, HTTPException
from app.config import settings
from app.schemas import ChatHistoryRequest, ChatAnalysisResponse, JobMatchRequest, JobMatchResponse
from app.services.vector_scan import vector_scanner
from app.services.llm_agent import LlmAgentService
from app.utils.helpers import clamp_score
from pydantic import BaseModel
from typing import List
import numpy as np
import requests
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import uvicorn
import traceback
import re

app = FastAPI(title = settings.APP_NAME, version = settings.VERSION)

@app.post("/chat", response_model = ChatAnalysisResponse)
async def analyze_compliance_dialogue(payload: ChatHistoryRequest):
    user_messages = [m.content for m in payload.history if m.role == "user"]
    if not user_messages:
        return ChatAnalysisResponse(
            agent_message = "I'm ready when you are. Please paste a job description or list your core responsibilities.",
            risk_score = 0,
            overall_risk_level = "Pending",
            requires_more_info = True,
            flags = []
        )
        
    latest_user_input = user_messages[-1]

    risk_score, risk_level, requires_more, flags = vector_scanner.scan(
        latest_user_input
    )

    formatted_flags = [f"- Flagged User Sentence: '{f.matched_text}'\n  Reason: {f.reason}" for f in flags]
    flag_context = "\n".join(formatted_flags)

    pipeline_result = await LlmAgentService.run_optimization_pipeline(latest_user_input, flag_context)

    verdict = pipeline_result.get("verdict", "SAFE")
    explanation = pipeline_result.get("explanation", "")
    optimized_text = pipeline_result.get("optimized_text", "")

    if verdict == "SAFE":
        risk_score = 0
        risk_level = "Safe"
        flags = []
        requires_more = False
    elif verdict == "LOW_RISK":
        risk_score = clamp_score(risk_score, 10, 19)
        risk_level = "Low"
    elif verdict ==  "MEDIUM_RISK":
        risk_score = clamp_score(risk_score, 20, 44)
        risk_level = "Medium"
    elif verdict == "CRITICAL_HIGH_RISK":
        risk_score = max(risk_score, 85)
        risk_level = "Critical"

    agent_display_message = (
        f"{explanation}\n\n"
        f"AUTOMATICALLY OPTIMIZED PROFILE VERSION:\n"
        f"```text\n{optimized_text}\n```"
    )

    return ChatAnalysisResponse(
        agent_message = agent_display_message,
        risk_score = risk_score,
        overall_risk_level = risk_level,
        requires_more_info = requires_more,
        flags = flags
    )

@app.post("/match", response_model=JobMatchResponse)
async def match_and_optimize_profile(payload: JobMatchRequest):
    """
    Exposes the production-grade matching endpoint. 
    Triggers the static vector pre-scan on the candidate's input profile text, 
    then processes the agentic dual-critic optimization loop.
    """
    _, _, _, flags = vector_scanner.scan(payload.candidate_profile)
    
    formatted_flags = [f"- Flagged Text Segment: '{f.matched_text}'\n Reason: {f.reason}" for f in flags]
    flag_context = "\n".join(formatted_flags)
    
    result = await LlmAgentService.run_matcher_pipeline(
        candidate_profile = payload.candidate_profile,
        job_description = payload.job_description,
        flag_context = flag_context
    )
    
    return JobMatchResponse(
        compliance_verdict = result.get("compliance_verdict", "SAFE"),
        overall_match_score = result.get("overall_match_score", 70),
        detected_gaps = result.get("detected_gaps", []),
        optimized_profile = result.get("optimized_profile", payload.candidate_profile)
    )

if __name__ == "__main__":
    uvicorn.run("app.main:app", host = "127.0.0.1", port = 8000, reload = True)