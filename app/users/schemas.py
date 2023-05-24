from pydantic import BaseModel


class UserInDB(BaseModel):
    id: int
    name: str
    token: str

    class Config:
        orm_mode = True


class UserOut(BaseModel):
    name: str
    token: str
