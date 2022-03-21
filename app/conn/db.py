from sqlalchemy import (Column, Integer, MetaData, String, Table,
                        create_engine, JSON)
# from databases import Database

from app.config import get_settings
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

settings = get_settings()
DATABASE_URL = f'mysql+mysqlconnector://{settings.db_user}:{settings.db_pass}@{settings.db_host}/{settings.db_schema}'


engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


