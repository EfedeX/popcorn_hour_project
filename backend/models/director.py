from datetime import date
from typing import Optional, List

from sqlmodel import SQLModel, Field, Relationship


class DirectorBase(SQLModel):
    name: str
    born_at: Optional[date] = None

class Director(DirectorBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    movies: List["Movie"] = Relationship(back_populates="director")

class DirectorCreate(DirectorBase):
    pass
