from typing import List

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session, select
from pydantic import BaseModel
from passlib.context import CryptContext

from ..models.user import UserBase, User
from ..utils import get_password_hash
from ..database import get_session
from ..auth import create_access_token

router = APIRouter(tags=["login"])
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
def home(session: Session = Depends(get_session)):
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

@router.post("/token")
def login_token(form_data: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_session)):
    user = session.exec(select(User).where(User.email == form_data.username)).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=400,
            detail="Incorrect email or password"
        )

    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer",
            "user_type": user.user_type}



