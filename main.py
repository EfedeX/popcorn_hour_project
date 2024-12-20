from contextlib import asynccontextmanager
import sys

from fastapi import FastAPI

from backend.database import create_db_and_tables, get_session
from backend.routes import users, login, directors, movies, images

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(users.router)
app.include_router(login.router)
app.include_router(directors.router)
app.include_router(movies.router)
app.include_router(images.router)
