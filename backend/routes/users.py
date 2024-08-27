from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from ..models.user import User, UserCreate
from ..utils import get_password_hash
from ..database import get_session

router = APIRouter()

@router.post("/users/", response_model=User)
def create_user(user: UserCreate, session: Session = Depends(get_session)):
    db_user = session.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = get_password_hash(user.password)
    db_user = User(email=user.email, hashed_password=hashed_password, user_type=user.user_type)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user
