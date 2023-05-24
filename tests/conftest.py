import os

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app import Base


@pytest.fixture(scope="module")
def session():
    engine = create_engine("sqlite:///test.db")
    Base.metadata.create_all(engine)
    connection = engine.connect()
    transaction = connection.begin()
    session_factory = sessionmaker(bind=connection)
    session = session_factory()

    yield session

    session.close()
    transaction.rollback()
    connection.close()
    os.remove("test.db")
