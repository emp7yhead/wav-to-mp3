from pydantic import BaseModel


class UserIn(BaseModel):
    id: int
    token: str


class UserOut(BaseModel):
    name: str
    token: str
