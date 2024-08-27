from sqlmodel import SQLModel, Field
from datetime import date


class Movie(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str = Field(index=True)
    release_date: date | None = None
    description: str | None = None
    genre: str | None = None
    director: str | None = None
    added_by: int = Field(foreign_key="user.id")
