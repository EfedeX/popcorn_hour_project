from datetime import date
from typing import Optional, List

from sqlmodel import SQLModel, Field, Relationship

from .director import DirectorCreate, DirectorBase

class MovieBase(SQLModel):
    title: str
    description: str
    release_date: Optional[date] = None
    genre: Optional[str] = None

class Movie(MovieBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    added_by_id: int = Field(foreign_key="user.id")
    added_by: Optional["User"] = Relationship(back_populates="movies")
    director_id: int = Field(foreign_key="director.id")
    director: Optional["Director"] = Relationship(back_populates="movies")
    ratings: List["Rating"] = Relationship(back_populates="movie")

    @property
    def average_rating(self) -> float:
        if not self.ratings:
            return 0.0
        return sum(r.score for r in self.ratings) / len(self.ratings)

class MovieCreate(MovieBase):
    director: DirectorCreate

class DirectorRead(DirectorBase):
    id: int

class MovieRead(MovieBase):
    id: int
    added_by_id: int
    director: DirectorRead
    average_rating: float

    class Config:
        from_attributes = True
