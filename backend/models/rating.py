from sqlmodel import Field, SQLModel
from datetime import datetime


class Rating(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    movie_id: int = Field(foreign_key='movie.id')
    user_id: int = Field(foreign_key='user.id')
    score: int = Field(ge=1, le=5)
    rated_at: datetime = Field(default_factory=datetime.utcnow)
