from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from decouple import config



DATABASE_URL=f"postgresql://{config('PSQL_USER')}:{config('PSQL_PASS')}@{config('PSQL_HOST')}:{config('PSQL_PORT')}/{config('PSQL_DB')}"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()