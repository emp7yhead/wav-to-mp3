from fastapi import APIRouter, Depends, Request, Response, UploadFile
from sqlalchemy.exc import DBAPIError
from sqlalchemy.orm.session import Session

from app.database import get_session
from app.records.schemas import RecordIn
from app.records.service import get_record, save_record
from app.records.utils import create_link, prepare_file
from app.users.service import is_authenticated

records_router = APIRouter(prefix='/records', tags=['records'])


@records_router.post('/')
def create_record(
    file: UploadFile,
    id: int,
    token: str,
    request: Request,
    db: Session = Depends(get_session),
):
    if not is_authenticated(db, id, token):
        return 404, {'error': 'Invalid user or token'}

    if not file.filename.endswith('.wav'):
        return 422, {'error': 'File must be wav format'}

    record_data: RecordIn = prepare_file(file)
    print(record_data.id)
    try:
        saved_record = save_record(db, id, record_data)
    except DBAPIError:
        return 500, {'error': 'Can\'t save record'}
    record_link = create_link(saved_record, request)
    print(record_link)
    return {'url': record_link}


@records_router.get(
    '/',
    responses={
        200: {
            "content": {"media/mpeg": {}}
        }
    },
    response_class=Response
)
def fetch_record(
    id: str,
    user: int,
    db: Session = Depends(get_session),
):
    record_entry = get_record(db, id, user)

    if not record_entry:
        return 404, {"error": "Record not found"}

    return Response(
        content=record_entry.data,
        media_type="media/mpeg",
        headers={'Content-Disposition': f'filename={id}.mp3'}
        )
