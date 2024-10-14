from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from pydantic import BaseModel
from passlib.context import CryptContext

from ..models.user import UserBase, User
from ..utils import get_password_hash
from ..database import get_session

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class LoginRequest(BaseModel):
    email: str
    password: str

def verify_password(
    plain_password: str,
    hashed_password: str
    ) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

@router.get("/")
def login(session: Session = Depends(get_session)):
    return {"message": "Welcome to the Popcorn Hour API!"}

@router.post("/login")
def login(request: LoginRequest,
    session: Session = Depends(get_session)
    ):
    user = session.query(User).filter(User.email == request.email).first()
    if user is None:
        raise HTTPException(status_code=401, detail="Invalid email or password")
    elif verify_password(request.password, user.hashed_password):
        return {"email": user.email, "message": "Login successful"}
    else:
        raise HTTPException(status_code=401, detail="Invalid email or password")


# if __name__ == "__main__":
#     pass

# https://fastapi.tiangolo.com/tutorial/bigger-applications/#another-module-with-apirouter
