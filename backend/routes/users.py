from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from ..models.user import User, UserCreate
from ..utils import get_password_hash
from ..database import get_session

router = APIRouter(
    prefix="/users"
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
    session.commit() # to create primary_key
    session.refresh(new_user) # to save it
    return new_user


@router.get("/", response_model=List[User])
def list_all_users(session: Session = Depends(get_session)):
    return session.execute(select(User)).all()
    # for user in users:
    #    print(users)

@router.get("/{email}", response_model=User)
def list_user(email: str, session: Session=Depends(get_session)):
    statement = select(User).where(User.email == email)
    return session.execute(statement)

@router.delete("/{email}")
def list_user(email: str, session: Session=Depends(get_session)):
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
