from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite:///./training.db"
engine = create_engine(DATABASE_URL)
session = sessionmaker(bind=engine)

Base = declarative_base()
