# Personal Finance API — Portfolio Project

An example, production-style backend for tracking simple finance items and users. This repository is packaged as a portfolio-ready project to demonstrate API design, testing, CI/CD, containerization, and deployment artifacts — everything clients expect from a modern backend.

Highlights
----------
- Runnable FastAPI backend with OpenAPI docs
- CI: Tests run on push/PR via GitHub Actions
- Dockerfile + `docker-compose.yml` for easy local deploy
- Minimal frontend demo and Kubernetes manifest for deployment
- Seed script and Postman collection for quick demos

Live demo (GitHub Pages): https://iruto607-debug.github.io/personal-finance-api/
- Static frontend is published from the `gh-pages` branch.
- If the page is not immediately live, enable GitHub Pages in repository settings and select the `gh-pages` branch.
GHCR image: ghcr.io/iruto607-debug/personal-finance-api:latest (published by workflow)

Render deploy
-------------

To enable a live API demo on Render and automatic deploys from `main`:

1. Create a Render service (see `docs/render-instructions.md` for detailed steps).
2. Add the repository secrets `RENDER_API_KEY` and `RENDER_SERVICE_ID` (Repository → Settings → Secrets → Actions).
3. Push to `main`; the `.github/workflows/deploy-render.yml` workflow will trigger and start a deploy.

I'll help you verify the deploy once you add those secrets — tell me when they're set and I'll trigger a run if needed.

![CI](https://github.com/iruto607-debug/personal-finance-api/actions/workflows/ci.yml/badge.svg)
![Lint](https://github.com/iruto607-debug/personal-finance-api/actions/workflows/lint.yml/badge.svg)
![Docker Image](https://github.com/iruto607-debug/personal-finance-api/packages/container/personal-finance-api/badge)

Why this project wins clients
----------------------------
- Clear README with quick-start and demo instructions
- Automated tests and linting in CI to ensure quality
- Containerized delivery for predictable deployments
- Example Kubernetes manifest and deploy instructions
- Clean, minimal API surface that is easy to extend

Quick start (local)
-------------------
1. Create a virtualenv and activate it

```bash
python -m venv .venv
.venv\Scripts\activate    # Windows
```

2. Install dependencies and run

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
# open http://localhost:8000/docs for API docs
```

Pre-commit
---------

Install pre-commit hooks locally before development:

```bash
pip install -r requirements-dev.txt
pre-commit install
pre-commit run --all-files
```

3. Seed sample data (creates `finance.db` with example rows)

```bash
python scripts/seed_data.py
```

Run with Docker
---------------

```bash
docker build -t personal-finance-api:local .
docker run -p 8000:8000 --env-file .env.example personal-finance-api:local
```

Run tests
---------

```bash
python -m pytest -q
```

API surface
-----------
- `GET /health` — health check
- `GET /users` — sample users
- `GET /finances` — sample finance items
- OpenAPI docs available at `/docs` and `/openapi.json`

Demo & Deliverables
-------------------
- Frontend demo: `frontend/index.html` (static single-page demo)
- Postman collection: `postman/personal-finance-api.postman_collection.json`
- K8s manifest: `k8s/deployment.yaml`
- Seed script: `scripts/seed_data.py`

Contact
-------
If you'd like to hire me to build or extend this project, email: iruto607@gmail.com — or open an issue / PR on GitHub.



