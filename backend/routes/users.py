from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from ..models.user import User, UserCreate, UserRead
from ..utils import get_password_hash
from ..database import get_session


router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.post("/", response_model=User)
def create_user(user: UserCreate,
    session: Session = Depends(get_session)
) -> User:
    db_user = session.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = get_password_hash(user.password)
    new_user = User(
        email=user.email,
        first_name=user.first_name,
        last_name=user.last_name,
        hashed_password=hashed_password,
        user_type=user.user_type
    )
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return new_user

@router.get("/", response_model=List[UserRead])
def list_all_users(session: Session = Depends(get_session)):
    users = session.execute(select(User)).scalars().all()
    return users

@router.get("/{email}", response_model=UserRead)
def list_user(email: str, session: Session=Depends(get_session)):
    statement = select(User).where(User.email == email)
    result = session.execute(statement).scalar_one_or_none()
    if result is None:
        raise HTTPException(status_code=404, detail="User not found")
    return result

@router.delete("/{email}")
def delete_user(email: str, session: Session=Depends(get_session)):
    statement = select(User).where(User.email == email)
    db_user = session.execute(statement)
    if not db_user:
        raise HTTPException(status_code=400, detail="Email does not exist!")
    session.delete(db_user)
    session.commit()
    session.refresh()


# router.patch() partial update
# router.put() full update
# router.delete() session.delete(user) instead of add
