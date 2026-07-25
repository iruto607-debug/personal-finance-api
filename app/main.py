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
        "<h1>Personal Finance API</h1><p>Welcome! Use <a href='/docs'>/docs</a> for API documentation.</p>"
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
