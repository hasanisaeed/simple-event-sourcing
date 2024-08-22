from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String, Numeric, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

DATABASE_URL = "postgresql://username:password@localhost/dbname"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# Event Store Model
class Event(Base):
    __tablename__ = 'events'

    event_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    event_type = Column(String(10), nullable=False)  # 'deposit' or 'withdrawal'
    amount = Column(Numeric(10, 2), nullable=False)
    event_time = Column(TIMESTAMP, default=datetime.datetime.utcnow)


Base.metadata.create_all(bind=engine)

app = FastAPI()
