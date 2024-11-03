from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.mysql import LONGBLOB
from typing import Optional



class Image(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    movie_id: int = Field(foreign_key="movie.id")
    movie: Optional["Movie"] = Relationship(back_populates="image")
    image_data: Optional[bytes] = Field(sa_column=Column(LONGBLOB), default=None)
    # image_data: Optional[bytes] = Field(
    #     sa_column=Column(LargeBinary), # only for sqlite AKA testing
    #     default=None
    # )
    content_type: Optional[str] = Field(default="image/jpeg")

class ImageRead(SQLModel):
    id: int
    movie_id: int
    content_type: Optional[str]
