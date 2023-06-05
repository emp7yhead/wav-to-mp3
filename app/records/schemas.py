from pydantic import BaseModel


class RecordIn(BaseModel):
    id: str
    data: bytes


class RecordOut(BaseModel):
    id: str
    user_id: int
    data: bytes
