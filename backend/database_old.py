from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 1. We swap the SQLite URL for the PostgreSQL one (pointing to Docker)
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:password123@localhost:5432/teamtrace"


# 2. We removed the SQLite-specific connect_args={"check_same_thread": False}
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()