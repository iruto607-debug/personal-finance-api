(# Personal Finance API)

Project description: a minimal API for tracking simple finance items and users. This repo is a portfolio-ready project with CI, Docker support, a frontend demo, and deployment manifests.

Quick start
----------

Run locally with Python:

```bash
python -m venv .venv
source .venv/Scripts/activate   # Windows
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Run with Docker:

```bash
docker build -t personal-finance-api:local .
docker run -p 8000:8000 --env-file .env.example personal-finance-api:local
```

Run tests:

```bash
python -m pytest -q
```

API endpoints
- `GET /health` — health check
- `GET /users` — sample users
- `GET /finances` — sample finance items

See `frontend/` for a minimal static demo and `k8s/` for a deployment manifest.

