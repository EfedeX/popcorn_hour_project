from sqlmodel import SQLModel, Field
from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import BYTEA


class Image(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    movie_id: int = Field(foreign_key="movie.id")
    image_data: bytes | None = Field(sa_column=Column(BYTEA), default=None)
