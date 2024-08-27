from sqlmodel import SQLModel, Field
from datetime import date


class Movie(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str = Field(index=True)
    release_date: date
    description: str
    genre: str
    director: str
    added_by: int = Field(foreign_key="user.id")
