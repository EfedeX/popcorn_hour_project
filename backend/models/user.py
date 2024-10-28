from datetime import datetime
from enum import Enum
from typing import Optional, List

from sqlmodel import SQLModel, Field, Relationship
from pydantic import EmailStr, BaseModel


class UserType(str, Enum):
    moderator = "moderator"
    standard = "standard"


class UserBase(SQLModel):
    first_name: str
    last_name: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: EmailStr = Field(unique=True, index=True)
    user_type: UserType = Field(default=UserType.standard)
    hashed_password: str
    movies: List["Movie"] = Relationship(back_populates="added_by")
    ratings: List["Rating"] = Relationship(back_populates="user")

class UserCreate(UserBase):
    email: EmailStr
    password: str
    user_type: UserType = Field(default=UserType.standard)

class UserRead(UserBase):
    id: int
    email: EmailStr
    user_type: UserType

