from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.orm import Session

from . import crud, database, models, schemas

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(
    title="Personal Finance API",
    description=(
        "A portfolio-ready example API for tracking users "
        "and finance items."
    ),
    version="1.0.0",
)


@app.get("/", response_class=HTMLResponse)
def root():
    return HTMLResponse(
        """
        <!doctype html>
        <html lang='en'>
          <head>
            <meta charset='utf-8' />
            <meta name='viewport' content='width=device-width,initial-scale=1' />
            <title>Personal Finance API</title>
            <style>
              body { font-family: Arial, sans-serif; max-width: 900px; margin: 2rem auto; padding: 0 1rem; background: #f4f7fb; color: #111; }
              header { margin-bottom: 1.5rem; }
              h1 { margin-bottom: 0.25rem; font-size: 2.25rem; }
              p, li { line-height: 1.75; }
              section { background: #ffffff; border: 1px solid #dce4ef; border-radius: 16px; padding: 1.6rem; box-shadow: 0 10px 30px rgba(15, 23, 42, 0.06); }
              .badge { display: inline-block; margin-right: 0.5rem; padding: 0.4rem 0.75rem; border-radius: 999px; background: #eef5ff; color: #1d4ed8; font-size: 0.9rem; }
              code { background: #eef1f8; padding: 0.2rem 0.4rem; border-radius: 5px; }
              pre { background: #f0f4ff; padding: 1rem; border-radius: 10px; overflow-x: auto; }
              a { color: #2563eb; text-decoration: none; }
              a:hover { text-decoration: underline; }
            </style>
          </head>
          <body>
            <header>
              <h1>Personal Finance API</h1>
              <p>A portfolio-ready backend for tracking users and finance items with FastAPI, SQLAlchemy, and containerized deployment.</p>
            </header>
            <section>
              <div class='badge'>Live API</div>
              <div class='badge'>FastAPI</div>
              <div class='badge'>Render ready</div>
              <p>This service is currently deployed on Render and provides a simple API for managing users and finance records.</p>
              <h2>Try the API</h2>
              <p>Use these endpoints directly, or open the OpenAPI docs:</p>
              <ul>
                <li><a href='/docs'>/docs</a> — interactive API documentation</li>
                <li><code>/health</code> — health check</li>
                <li><code>/users</code> — list users</li>
                <li><code>/finances</code> — list finance items</li>
              </ul>
              <pre>curl https://personal-finance-api-hrlq.onrender.com/health
curl https://personal-finance-api-hrlq.onrender.com/users
curl https://personal-finance-api-hrlq.onrender.com/finances</pre>
              <p>For local development, run the backend and use <code>http://localhost:8000</code> instead.</p>
            </section>
          </body>
        </html>
        """
    )


@app.get("/favicon.ico")
def favicon():
    return RedirectResponse(url="/docs/favicon.ico")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/users", response_model=list[schemas.UserResponse])
def read_users(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(database.get_db),
):
    return crud.get_users(db, skip=skip, limit=limit)


@app.post("/users", response_model=schemas.UserResponse, status_code=201)
def create_user(
    user: schemas.UserCreate, db: Session = Depends(database.get_db)
):
    if crud.get_user_by_email(db, user.email):
        raise HTTPException(
            status_code=400, detail="User email already exists"
        )
    return crud.create_user(db, user)


@app.get("/users/{user_id}", response_model=schemas.UserResponse)
def read_user(user_id: int, db: Session = Depends(database.get_db)):
    user = crud.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.get("/finances", response_model=list[schemas.FinanceResponse])
def read_finances(
    user_id: int | None = None,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(database.get_db),
):
    return crud.get_finances(db, user_id=user_id, skip=skip, limit=limit)


@app.post("/finances", response_model=schemas.FinanceResponse, status_code=201)
def create_finance(
    finance: schemas.FinanceCreate, db: Session = Depends(database.get_db)
):
    if not crud.get_user(db, finance.user_id):
        raise HTTPException(status_code=404, detail="User not found")
    return crud.create_finance(db, finance)
