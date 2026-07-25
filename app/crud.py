from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: int):
    user = get_user(db, user_id)

    if user:
        db.delete(user)
        db.commit()

    return user


def get_finance(db: Session, finance_id: int):
    return (
        db.query(models.Finance)
        .filter(models.Finance.id == finance_id)
        .first()
    )


def get_finances(
    db: Session, user_id: int | None = None, skip: int = 0, limit: int = 100
):
    query = db.query(models.Finance)
    if user_id is not None:
        query = query.filter(models.Finance.user_id == user_id)
    return query.offset(skip).limit(limit).all()


def create_finance(db: Session, finance: schemas.FinanceCreate):
    db_finance = models.Finance(**finance.dict())
    db.add(db_finance)
    db.commit()
    db.refresh(db_finance)
    return db_finance
