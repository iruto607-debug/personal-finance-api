from sqlalchemy import Column, Float, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine(
    "sqlite:///startup.db", connect_args={"check_same_thread": False}
)
Base = declarative_base()
Session = sessionmaker(bind=engine)
db = Session()


class User(Base):
    __tablename__ = "users"

    username = Column(String, primary_key=True)
    password = Column(String)


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    date = Column(String)
    type = Column(String)
    category = Column(String)
    amount = Column(Float)


Base.metadata.create_all(engine)
