import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = os.getenv("DATABASE_URL") or "sqlite:///./Housekeeping.db" # provided by Render
    # Default to SQLite db if DATABASE_URL is not set (e.g. when running locally)

engine = create_engine(DATABASE_URL) 

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()