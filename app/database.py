from typing import Any, Generator

from sqlalchemy import Engine, create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import declarative_base, scoped_session, sessionmaker
from sqlalchemy.orm.session import Session

from app.settings import settings

engine: Engine = create_engine(
    settings.SQLALCHEMY_DATABASE_URI,
)

SessionLocal: scoped_session[Session] = scoped_session(
    sessionmaker(expire_on_commit=False, autoflush=False, bind=engine)
)

Base: Any = declarative_base()


def get_session() -> Generator[Session, Any, None]:
    session: Session = SessionLocal()
    try:
        yield session
        session.commit()
    except IntegrityError:
        session.rollback()
        pass
    finally:
        session.close()
