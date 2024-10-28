from typing import List
from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from sqlalchemy.orm import selectinload
from sqlalchemy import func

from ..database import get_session
from ..auth import get_current_user
from ..models.movie import Movie, MovieCreate, MovieRead
from ..models.rating import Rating, RatingCreate, RatingRead
from ..models.user import User
from ..models.director import Director


router = APIRouter(prefix="/movies", tags=["movies"])

@router.post("/", response_model=MovieRead)
def create_movie(
    movie: MovieCreate,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
) -> Movie:
    if current_user.user_type != "moderator":
        raise HTTPException(
            status_code=403,
            detail="Only moderators can create movies"
        )

    db_movie = session.exec(
        select(Movie).where(func.lower(Movie.title) == movie.title.lower())
    ).first()

    if db_movie:
        raise HTTPException(status_code=400, detail="Movie already registered")

    db_director = session.exec(
        select(Director).where(func.lower(Director.name) == movie.director.name.lower())
    ).first()

    if not db_director:
        db_director = Director(
            name=movie.director.name.title(),
            born_at=movie.director.born_at
        )
        session.add(db_director)
        session.flush()

    new_movie = Movie(
        title=movie.title.title(),
        description=movie.description,
        release_date=movie.release_date,
        genre=movie.genre,
        added_by_id=current_user.id,
        director_id=db_director.id
    )

    session.add(new_movie)
    session.commit()
    session.refresh(new_movie)
    return new_movie

@router.get("/{movie_id}", response_model=Movie)
def get_movie(
    movie_id: int,
    session: Session = Depends(get_session)
):
    statement = select(Movie).where(Movie.id == movie_id)
    return session.execute(statement)

# endpoints para ratings
@router.post("/{movie_id}/rate", response_model=RatingRead)
def rate_movie(
    movie_id: int,
    rating: RatingCreate,
    session: Session = Depends(get_session)
):
    movie = session.get(Movie, movie_id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    existing_rating = session.exec(
        select(Rating)
        .where(Rating.movie_id == movie_id)
    ).first()

    if existing_rating:
        existing_rating.score = rating.score
        existing_rating.rated_at = datetime.utcnow()
        session.add(existing_rating)
        session.commit()
        session.refresh(existing_rating)
        return existing_rating

    db_rating = Rating(
        movie_id=movie_id,
        user_id=1, ## CHAAANGE THIIIIIS
        score=rating.score
    )
    session.add(db_rating)
    try:
        session.commit()
        session.refresh(db_rating)
    except IntegrityError:
        session.rollback()
        raise HTTPException(
            status_code=400,
            detail="You have already rated this movie"
        )
    return db_rating

@router.get("/{movie_id}/ratings", response_model=List[RatingRead])
def get_movie_ratings(
    movie_id: int,
    session: Session = Depends(get_session)
):
    movie = session.get(Movie, movie_id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")

    ratings = session.exec(
        select(Rating)
        .where(Rating.movie_id == movie_id)
        .order_by(Rating.rated_at.desc())
    ).all()
    return ratings

@router.get("/{movie_id}/average-rating")
def get_movie_average_rating(
    movie_id: int,
    session: Session = Depends(get_session)
):
    movie = session.exec(
        select(Movie)
        .where(Movie.id == movie_id)
        .options(selectinload(Movie.ratings))
    ).first()
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")

    return {
        "movie_id": movie_id,
        "average_rating": movie.average_rating,
        "total_ratings": len(movie.ratings)
    }
