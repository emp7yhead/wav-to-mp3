from fastapi import Request, UploadFile
from pydub import AudioSegment

from app.records.schemas import RecordIn, RecordOut
from app.users.utils import create_token


def convert_wav_to_mp3(wav_file: UploadFile) -> bytes:
    mp3_data = AudioSegment.from_wav(
        wav_file.file,
    ).export(format="mp3").read()
    return mp3_data


def prepare_file(wav_file: UploadFile) -> RecordIn:
    mp3_data = convert_wav_to_mp3(wav_file)
    unique_token = create_token()
    print(unique_token)
    return RecordIn(id=unique_token, data=mp3_data)


def create_link(record_data: RecordOut, request: Request) -> str:
    url = request.url
    path = url.path
    scheme = url.scheme
    host = url.hostname
    port = url.port
    return f"{scheme}://{host}:{port}{path}?id={record_data.id} \
        &user={record_data.user_id}"
