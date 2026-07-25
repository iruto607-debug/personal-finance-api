from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Personal Finance API")


class User(BaseModel):
    id: int
    name: str


class FinanceItem(BaseModel):
    id: int
    user_id: int
    amount: float
    description: str | None = None


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/users")
def list_users():
    return [User(id=1, name="Alice"), User(id=2, name="Bob")]


@app.get("/finances")
def list_finances():
    return [
        FinanceItem(id=1, user_id=1, amount=1200.0, description="Salary"),
        FinanceItem(id=2, user_id=1, amount=-50.0, description="Groceries"),
    ]
