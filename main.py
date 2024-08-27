from contextlib import asynccontextmanager

from fastapi import FastAPI

from backend.database import create_db_and_tables, get_session
from backend.routes import users

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(users.router)

@app.get('/users')
def list_moderators():
    return 'hello'
# @app.on_event("startup")
# def on_startup():
#     create_db_and_tables()
