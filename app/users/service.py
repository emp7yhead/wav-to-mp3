from sqlalchemy import insert
from sqlalchemy.orm.session import Session

from app import User


def create_new_user(session: Session, name: str, token: str) -> User:
    return session.execute(
            insert(User).returning(User), {
                'name': name,
                'token': token,
            }
        ).scalar()
