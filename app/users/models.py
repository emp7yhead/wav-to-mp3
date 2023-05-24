from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        autoincrement=True, primary_key=True, index=True
    )
    name: Mapped[str]
    token: Mapped[str]

    def __str__(self) -> str:
        return f'id: {self.id} \
            name: {self.name} \
            token: {self.token}'
