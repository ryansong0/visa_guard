import sys, asyncio, re
sys.path.insert(0, ".")
from app.services.llm_agent import LlmAgentService

resume = "Senior Software Engineer with 5 years of experience. Led the design and implementation of a payment processing service handling high transaction volume. Mentored 2 junior engineers on code quality practices. Built services in Python and Go. Skills: Python, Go, Kubernetes, mentorship."

WORD_RE = re.compile(r'\b(managed|led|directed|overseeing|oversaw)\b', re.IGNORECASE)

async def main():
    for i in range(3):
        rewritten = await LlmAgentService.run_rewrite_pipeline(resume, [])
        print(f"--- attempt {i} ---")
        print(rewritten)
        print("substring 'led' present:", "led" in rewritten.lower())
        print("word-boundary match:", WORD_RE.findall(rewritten))

asyncio.run(main())
