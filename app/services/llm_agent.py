import httpx
import json
import logging
from typing import Dict, Any
from app.config import settings
from app.utils.helpers import clamp_score
from app.schemas import ChatAnalysisResponse, RiskFlag

logging.basicConfig(level = logging.INFO)
logger = logging.getLogger("VisalifyAgent")

class LlmAgentService:
    @staticmethod
    def _get_structured_schema() -> Dict[str, Any]:
        """Defines the strict JSON schema the LLM MUST return."""
        return {
            "type": "object",
            "properties": {
                "verdict": {"type": "string", "enum": ["CRITICAL_HIGH_RISK", "MEDIUM_RISK", "LOW_RISK", "SAFE"]},
                "explanation": {"type": "string"},
                "optimized_text": {"type": "string", "description": "The rewritten, compliant version of the input data"}
            },
            "required": ["verdict", "explanation", "optimized_text"]
        }  

    @staticmethod
    def _get_matcher_schema() -> Dict[str, Any]:
        """Defines the strict JSON schema for the dual profile + job description optimization pipeline."""
        return {
            "type": "object",
            "properties": {
                "compliance_verdict": {"type": "string", "enum": ["CRITICAL_HIGH_RISK", "MEDIUM_RISK", "LOW_RISK", "SAFE"]},
                "overall_match_score": {"type": "integer", "minimum": 0, "maximum": 100},
                "detected_gaps": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "category": {"type": "string", "enum": ["Regulatory Compliance Risk", "Technical Skill Gap"]},
                            "detected_risk": {"type": "string"},
                            "optimization_strategy": {"type": "string"}
                        },
                        "required": ["category", "detected_risk", "optimization_strategy"]
                    }
                },
                "optimized_profile": {"type": "string"}
            },
            "required": ["compliance_verdict", "overall_match_score", "detected_gaps", "optimized_profile"]
        } 

    @classmethod
    async def run_optimization_pipeline(cls, latest_input: str, flag_context: str) -> Dict[str, Any]:
        """Legacy standalone profile optimization pipeline (Keep this active for backward compatibility)."""
        system_prompt = f"You are Visalify AI. Analyze this profile against compliance flags:\n{flag_context}"
        payload = {
            "model": settings.LLM_MODEL,
            "prompt": f"{system_prompt}\n\nCandidate Profile Input: {latest_input}",
            "stream": False,
            "format": cls._get_structured_schema()
        }
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(f"{settings.OLLAMA_URL}/api/generate", json=payload, timeout=60.0)
                if response.status_code == 200:
                    return json.loads(response.json().get("response", "{}"))
            except Exception as e:
                logger.error(f"Legacy Pipeline Failure: {e}")
            return {"verdict": "SAFE", "explanation": "Fallback active.", "optimized_text": latest_input}
        
        
    @classmethod
    async def run_matcher_pipeline(cls, candidate_profile: str, job_description: str, flag_context: str) -> Dict[str, Any]:
        """
        STAGE 1 & STAGE 2 DUAL-CRITIC OPTIMIZATION PIPELINE.
        Intersects the profile with real-world job requirements while enforcing regulatory parameters.
        """
        logger.info("Executing Dual-Critic Job Matching and Compliance Optimization Loop...")

        system_prompt = f"""
        You are the core intelligence engine of Visalify—an advanced AI agent optimizing candidate profiles for job market fit and immigration compliance (8 CFR 214.6 guidelines).
        
        You have two core tasks that you must balance simultaneously:
        1. SKILL GAP ANALYTICS: Compare the Candidate Profile with the target Job Description. Identify keywords, software architectures, or tools missing from the profile.
        2. COMPLIANCE ENFORCEMENT: Cross-reference the text with our vector pre-scanner anomalies:
           {flag_context if flag_context else "No static anomalies found."}
           Ensure the profile does not claim non-compliant attributes (e.g., executing day-to-day corporate operations or cross-functional people management for technical TN tracks).
        
        STAGES OF EXECUTION:
        - STAGE 1 (DUAL CRITIQUE): Evaluate gaps. Populate 'detected_gaps' choosing either 'Regulatory Compliance Risk' or 'Technical Skill Gap' for categories.
        - STAGE 2 (DYNAMIC REWRITE): Rewrite the candidate's profile into 'optimized_profile'. Inject highly relevant technical keywords matching the job description while aggressively scrubbing out or reframing high-risk management verbiage into compliant systems engineering terminology.

        You MUST respond strictly with a valid JSON object matching the requested schema. Do not include markdown blocks like ```json.
        """

        url = f"{settings.OLLAMA_URL}/api/generate"
        payload = {
            "model": settings.LLM_MODEL,
            "prompt": f"{system_prompt}\n\n[CANDIDATE PROFILE]:\n{candidate_profile}\n\n[TARGET JOB DESCRIPTION]:\n{job_description}",
            "stream": False,
            "format": cls._get_matcher_schema()
        }

        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(url, json = payload, timeout = 60.0)
                if response.status_code == 200:
                    raw_data = response.json().get("response", "{}")
                    logger.info("Successfully received structured matcher payload.")
                    return json.loads(raw_data)
            except Exception as e:
                logger.error(f"Dual Matcher Pipeline Trace Failure: {e}")
            
            return {
                "compliance_verdict": "SAFE",
                "overall_match_score": 50,
                "detected_gaps": [{"category": "Technical Skill Gap", "detected_risk": "Pipeline tracking fault.", "optimization_strategy": "Verify Ollama connectivity."}],
                "optimized_profile": candidate_profile
            }