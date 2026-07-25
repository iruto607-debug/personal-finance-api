# Deploying to Render — setup instructions

Follow these steps to create a Render service and enable automatic deployments from this repository.

1. Create a Render account (https://render.com) and log in.
2. Create a new Web Service on Render:
   - Environment: <choose "Docker" or "Static Site" depending on which you want to deploy.>
   - If deploying the API: choose "Web Service" and select Docker; set the start command to `uvicorn app.main:app --host 0.0.0.0 --port 8000`.
   - For the frontend static demo, choose "Static Site" and set the publish directory to `/frontend`.
3. After creating the service, get the Service ID from the service's settings page (the ID is visible in the URL or on the service's API settings page).
4. Create an API key for your account: Account → API Keys → Create Key. Copy the key immediately.
5. Add two GitHub repository secrets:
   - `RENDER_API_KEY` — the API key you created.
   - `RENDER_SERVICE_ID` — the service ID for the Render service you want to trigger.
   Add them in the repository: Settings → Secrets and variables → Actions → New repository secret.
6. After adding the secrets, push to `main`.
7. Go to GitHub Actions → Deploy to Render and confirm the workflow succeeds.
   - If it fails, open the log and look for "ERROR: RENDER_API_KEY or RENDER_SERVICE_ID not set." or the Render API response.
8. Confirm the deploy in the Render dashboard; note the service URL (e.g., `https://your-service.onrender.com`) and share it in the README or landing page.

Notes
- For multi-environment deployments (staging/production), create separate services and use separate secrets.
- If you prefer full control, you can also connect GitHub directly from Render's dashboard (Render will set up deploys without needing the API key). The workflow provides a lightweight trigger alternative.
