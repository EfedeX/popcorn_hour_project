import os

from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv

from .models.user import User
from .models.movie import Movie
from .models.image import Image
from .models.comment import Comment
from .models.rating import Rating

dotenv_path = os.path.join(os.path.dirname(__file__), '../.env')

load_dotenv(dotenv_path)


DATABASE_URL = os.getenv('DATABASE_URL')
engine = create_engine(DATABASE_URL)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
