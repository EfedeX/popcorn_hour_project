from fastapi import FastAPI

from .database import create_db_and_tables
from .routes import users


app = FastAPI()
app.include_router(users.router)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()
