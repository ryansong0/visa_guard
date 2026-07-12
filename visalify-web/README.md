# Visalify (Next.js frontend)

## Setup

```bash
npm install
cp .env.local.example .env.local   # edit NEXT_PUBLIC_API_URL if needed
npm run dev
```

Visit http://localhost:3000

## Backend requirement

Your FastAPI backend must:
1. Run on the URL set in `NEXT_PUBLIC_API_URL` (default `http://127.0.0.1:8000`)
2. Expose `POST /match` accepting `{ candidate_profile, job_description }`
   and returning `{ overall_match_score, compliance_verdict, detected_gaps, optimized_profile }`
3. Enable CORS for `http://localhost:3000` (see FastAPI snippet below)

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)
```
