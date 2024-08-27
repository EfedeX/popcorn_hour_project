import sys
sys.path.append("..")

from sqlmodel import Session
from backend.database import engine, create_db_and_tables
from backend.models.user import User, UserType
from backend.utils import get_password_hash


def create_moderator(email: str, password: str):
    create_db_and_tables()

    with Session(engine) as session:
        user = User(
            email=email,
            hashed_password=get_password_hash(password),
            user_type=UserType.moderator
        )
        session.add(user)
        session.commit()
        print(f"Moderator user created: {email}")


if __name__ == "__main__":
    email = input("Enter moderator email: ")
    password = input("Enter moderator password: ")
    create_moderator(email, password)
