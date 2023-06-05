from pydantic import BaseModel


class UserIn(BaseModel):
    name: str
    token: str


class UserOut(BaseModel):
    id: int
    token: str
