from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.records.models import Record


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        autoincrement=True, primary_key=True, index=True
    )
    name: Mapped[str]
    token: Mapped[str]
    records: Mapped[list["Record"] | None] = relationship(
        cascade="all, delete-orphan"
    )

    def __str__(self) -> str:
        return f'id: {self.id} \
            name: {self.name} \
            token: {self.token}'

    def to_dict(self) -> dict:
        return {
            field.name: getattr(self, field.name)
            for field in self.__table__.c
        }
