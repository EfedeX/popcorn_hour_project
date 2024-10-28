import os

from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
print(dotenv_path)
load_dotenv(dotenv_path)

DATABASE_URL = os.getenv('DATABASE_URL')
engine = create_engine("sqlite:///./test.db", echo=True) # change to DATABASE_URL later

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
