from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .config import settings

DATABASE_URL = settings.DATABASE_URL

if not DATABASE_URL:
    raise ValueError('DATABASE_URL environment variable is not set or is None')

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)