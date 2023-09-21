from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import settings

SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.PG_USER}:{settings.PG_PASSWORD}@{settings.PG_HOST}:{settings.PG_PORT}/{settings.PG_DB_NAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
