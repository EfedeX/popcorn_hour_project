from sqlmodel import SQLModel, Field
from datetime import datetime


class Comment(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    movie_id: int = Field(foreign_key="movie.id")
    user_id: int = Field(foreign_key="user.id")
    content: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
