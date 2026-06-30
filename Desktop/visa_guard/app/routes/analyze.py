from fastapi import APIRouter
from app.services.analyzer import analyze_text

router = APIRouter()

@router.post("/analyze")
def analyze(data: dict):
    job_description = data.get("job_description", "")

    findings = analyze_text(job_description)

    analysis_results = analyze_text(job_description)

    return analysis_results