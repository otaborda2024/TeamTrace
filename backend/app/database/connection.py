from sqlalchemy import create_engine


DATABASE_URL = "postgresql://postgres:password123@localhost:5432/teamtrace"


engine = create_engine(DATABASE_URL)
