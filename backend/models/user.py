from datetime import datetime
from enum import Enum
from typing import Optional

from sqlmodel import SQLModel, Field
from pydantic import EmailStr


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

class UserCreate(UserBase):
    email: EmailStr
    password: str
    user_type: UserType = Field(default=UserType.standard)
