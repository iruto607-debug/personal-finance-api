from pathlib import Path

from app import crud, database, models, schemas

DB_PATH = Path(__file__).resolve().parents[1] / "finance.db"


def seed():
    models.Base.metadata.create_all(bind=database.engine)
    db = database.SessionLocal()
    try:
        db.query(models.Finance).delete()
        db.query(models.User).delete()

        alice = crud.create_user(
            db, schemas.UserCreate(name="Alice", email="alice@example.com")
        )
        bob = crud.create_user(
            db, schemas.UserCreate(name="Bob", email="bob@example.com")
        )

        crud.create_finance(
            db,
            schemas.FinanceCreate(
                user_id=alice.id,
                amount=1200.0,
                description="Salary",
            ),
        )
        crud.create_finance(
            db,
            schemas.FinanceCreate(
                user_id=alice.id,
                amount=-50.0,
                description="Groceries",
            ),
        )
        crud.create_finance(
            db,
            schemas.FinanceCreate(
                user_id=bob.id,
                amount=-20.5,
                description="Coffee",
            ),
        )
    finally:
        db.close()

    print(f"Seeded database at: {DB_PATH}")


if __name__ == "__main__":
    seed()
