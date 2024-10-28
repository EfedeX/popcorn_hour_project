from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel, Relationship, UniqueConstraint


class RatingBase(SQLModel):
    score: int = Field(ge=1, le=5)  # Rating de 1 a 5 estrellas
    rated_at: datetime = Field(default_factory=datetime.utcnow)

class Rating(RatingBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    movie_id: int = Field(foreign_key="movie.id")
    user_id: int = Field(foreign_key="user.id")
    movie: "Movie" = Relationship(back_populates="ratings")
    user: "User" = Relationship(back_populates="ratings")
    #  Constraint para asegurar que un usuario solo pueda calificar una peli una vez
    __table_args__ = (
        UniqueConstraint("user_id", "movie_id", name="unique_user_movie_rating"),
    )

class RatingCreate(RatingBase):
    movie_id: int

class RatingRead(RatingBase):
    id: int
    movie_id: int
    user_id: int
