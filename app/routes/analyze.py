from fastapi import APIRouter
from app.services.analyzer import rules_engine
from pydantic import BaseModel
from typing import List, Dict
import json

router = APIRouter()

class ChatSessionPayload(BaseModel):
    history: List[Dict[str, str]]

@router.post("/analyze")
def analyze(data: dict):
    job_description = data.get("job_description", "")

    findings = rules_engine(job_description)

    analysis_results = rules_engine(job_description)

    return analysis_results