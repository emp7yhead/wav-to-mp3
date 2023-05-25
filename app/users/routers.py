from http import HTTPStatus

from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

from app import User
from app.database import get_session
from app.users.schemas import UserOut
from app.users.service import create_new_user
from app.users.utils import create_token

users_router = APIRouter(prefix='/users', tags=['users'])


@users_router.post(
    '/',
    status_code=HTTPStatus.CREATED,
    response_model=UserOut,
)
async def create_user(
    name: str,
    db: Session = Depends(get_session)
):
    token: str = create_token()
    new_user: User = create_new_user(db, name=name, token=token)
    return UserOut(**new_user.to_dict())
