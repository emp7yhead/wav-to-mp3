from sqlalchemy import insert, select
from sqlalchemy.orm.session import Session

from app.records.models import Record
from app.records.schemas import RecordIn


def save_record(
    session: Session,
    user_id: int,
    record_data: RecordIn
):
    return session.execute(
        insert(Record)
        .returning(Record.id, Record.user_id)
        .values(id=record_data.id, data=record_data.data, user_id=user_id)
    ).one_or_none()


def get_record(
    session: Session,
    record_id: str,
    user_id: int,
) -> Record | None:
    return session.execute(
        select(Record)
        .where(Record.id == record_id, Record.user_id == user_id)
    ).scalar_one_or_none()
