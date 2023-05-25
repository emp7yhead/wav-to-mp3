from sqlalchemy import ForeignKey
from app import Base
from sqlalchemy.orm import Mapped, mapped_column


class Record(Base):
    __tablename__ = "records"
    id: Mapped[int] = mapped_column(
        autoincrement=True, primary_key=True, index=True
    )
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    _id: Mapped[int]
    data: Mapped[bytes]
