from sqlalchemy import Select, insert, select
from sqlalchemy.orm.session import Session

from app import User
from app.users.schemas import UserIn


def create_new_user(session: Session, name: str, token: str) -> User | None:
    return session.execute(
            insert(User).returning(User), {
                'name': name,
                'token': token,
            }
        ).scalar()


def get_user(session: Session, id: int) -> User | None:
    stmt: Select = select(User).where(User.id == id)
    return session.scalars(stmt).one_or_none()


def is_authenticated(db, id, token) -> bool:
    current_user = get_user(db, id)
    return current_user or current_user.token == token
