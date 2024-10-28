from typing import List

from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from ..models.director import Director, DirectorCreate
from ..database import get_session


router = APIRouter(
    prefix="/directors",
    tags=["directors"]
)

@router.post("/", response_model=Director)
def create_director(director: DirectorCreate,
    session: Session = Depends(get_session)
) -> Director:
    db_director = (session.query(Director).filter(
        Director.first_name.title() == director.first_name.title(),
        Director.last_name.title() == director.last_name.title()
        )
        .first()
    )
    if db_director:
        pass # Add movie to director
    else:
        new_director = Director(
        first_name=director.first_name,
        last_name=director.last_name,
        born_at=director.born_at
    )
    session.add(new_director)
    session.commit()
    session.refresh(new_director)
    return new_director

@router.get("/", response_model=List[Director])
def list_50_directors(session: Session = Depends(get_session)):
    directors = session.execute(select(Director)).limit(50).scalars().all()
    return directors

@router.get("/{id}", response_model=Director)
def list_director(id: int, session: Session=Depends(get_session)):
    statement = select(Director).where(Director.email == id)
    return session.execute(statement)

@router.delete("/{id}")
def delete_director(id: int, session: Session=Depends(get_session)):
    statement = select(User).where(Director.id == id)
    db_director = session.execute(statement)
    if not db_director:
        raise HTTPException(status_code=400, detail="Director does not exist!")
    session.delete(db_director)
    session.commit()
    session.refresh()


# router.patch() partial update
# router.put() full update
# router.delete() session.delete(user) instead of add
