from fastapi import APIRouter, HTTPException, Response, Depends, Form, UploadFile, File
from sqlmodel import Session, select
from typing import Optional

from ..database import get_session
from ..models.image import Image
from ..models.movie import Movie

router = APIRouter(
            prefix='/images',
            tags=["image"]
)

@router.get("/{image_id}")
def get_image(
    image_id: int,
    session: Session = Depends(get_session)
):
    result = session.execute(select(Image).where(Image.id == image_id))
    image = result.scalars().first()

    if not image:
        raise HTTPException(status_code=404, detail="Image not found")

    return Response(content=image.image_data, media_type=image.content_type)

@router.post("/")
async def upload_image(
    movie_id: int = Form(...),
    description: Optional[str] = Form(None),
    image: UploadFile = File(...),
    session: Session = Depends(get_session)
):
    movie = session.get(Movie, movie_id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")

    contents = await image.read()

    image_data = Image(
        movie_id=movie_id,
        description=description,
        image_data=contents,
        content_type=image.content_type
    )

    session.add(image_data)
    session.commit()
    session.refresh(image_data)

    return {"id": image_data.id}

@router.get("/movie/{movie_id}")
def get_image_by_movie_id(
    movie_id: int,
    session: Session = Depends(get_session)
):
    result = session.execute(select(Image).where(Image.movie_id == movie_id))
    image = result.scalars().first()

    if not image:
        raise HTTPException(status_code=404, detail="Image not found")

    return Response(content=image.image_data, media_type=image.content_type)
