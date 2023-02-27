from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.ext.declarative import declarative_base

SQL_ALCHEMY_DATABASE_URL = 'sqlite:///./todos.db'

engine = create_engine(url=SQL_ALCHEMY_DATABASE_URL,
                       connect_args= {'check_same_thread': False}
                       )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()