from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from ..models.user import UserBase, User
from ..utils import get_password_hash
from ..database import get_session

router = APIRouter()

@router.get("/")
def login(session: Session = Depends(get_session)):
    return {"message": "Welcome to the Popcorn Hour API!"}
    # session.add(db_user)
    # session.commit() # to create primary_key
    # session.refresh(db_user) # to save it
    # return db_user


# if __name__ == "__main__":
#     pass

# https://fastapi.tiangolo.com/tutorial/bigger-applications/#another-module-with-apirouter
