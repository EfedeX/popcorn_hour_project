from datetime import datetime
from enum import Enum

from sqlmodel import SQLModel, Field
from pydantic import EmailStr


class UserType(str, Enum):
    moderator = "moderator"
    standard = "standard"


class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    email: EmailStr = Field(unique=True, index=True)
    hashed_password: str
    user_type: UserType = Field(default=UserType.standard)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class UserCreate(SQLModel):
    email: EmailStr
    password: str
    user_type: UserType = UserType.standard
