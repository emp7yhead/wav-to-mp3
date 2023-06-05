from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app import Base


class Record(Base):
    __tablename__ = "records"
    id: Mapped[str] = mapped_column(
        primary_key=True, index=True
    )
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    data: Mapped[bytes]
