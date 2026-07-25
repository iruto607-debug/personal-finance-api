# Deployment Status

## Live frontend demo
- **GitHub Pages** is published from the `gh-pages` branch.
- Live demo URL: `https://iruto607-debug.github.io/personal-finance-api/`
- The site serves the static frontend demo from `frontend/index.html`.

## Backend deployment
- The repository includes a Render deploy workflow at `.github/workflows/deploy-render.yml`.
- To activate the backend API deploy, add the following GitHub repository secrets:
  - `RENDER_API_KEY`
  - `RENDER_SERVICE_ID`
- Once the secrets are added, a push to `main` will trigger the deploy workflow automatically.

## CI and packaging
- Continuous integration runs on `main` for both `push` and `pull_request` events.
- The workflow installs dependencies and runs tests using `pytest`.
- A GitHub Container Registry image is published by the `publish-image.yml` workflow.

## Notes for portfolio reviewers
- The live static demo is already available on GitHub Pages.
- The backend API can be deployed with Render for a full live service.
- The repo also includes Docker, Docker Compose, Kubernetes manifest, and Postman assets for a complete delivery story.
