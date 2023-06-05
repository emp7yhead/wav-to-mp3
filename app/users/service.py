from sqlalchemy import Select, insert, select
from sqlalchemy.orm.session import Session

from app import User


def create_new_user(session: Session, name: str, token: str) -> User:
    return session.execute(
            insert(User).returning(User), {
                'name': name,
                'token': token,
            }
        ).scalar()


def get_user(session: Session, id: int) -> User | None:
    stmt: Select = select(User).where(User.id == id)
    return session.scalars(stmt).one_or_none()


def is_authenticated(session: Session, id: int, token: str) -> bool:
    current_user: User | None = get_user(session, id)
    if not current_user:
        return False
    return current_user.token == token
