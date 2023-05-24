from sqlalchemy.orm.session import Session
from app.users.utils import create_token
from app.users.service import create_new_user


def test_create_new_user(session: Session):
    test_token = create_token()
    test_name = 'Test'
    test_user = create_new_user(session, test_name, test_token)
    assert test_user.id == 1
    assert test_user.name == test_name
    assert test_user.token == test_token
