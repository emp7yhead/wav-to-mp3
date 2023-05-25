import io
from fastapi import UploadFile
from pydub import AudioSegment
from pathlib import Path
from app.records.utils import convert_wav_to_mp3


def get_fixture_path(filename: str) -> Path:
    fixtures_path: str = 'tests/fixtures'
    return Path(fixtures_path, filename).absolute()


def get_fixture_data(fixture_path: Path) -> bytes:
    with open(fixture_path, 'rb') as data:
        return data.read()


def get_fixture_file(fixture_data: bytes) -> UploadFile:
    return UploadFile(file=io.BytesIO(fixture_data), filename="sample.wav")


def create_fixture(filename: str) -> UploadFile:
    fixture_path = get_fixture_path(filename)
    fixture_data = get_fixture_data(fixture_path)
    return get_fixture_file(fixture_data)


def test_convert():
    test_wav_file = create_fixture('sample.wav')
    mp3_data = convert_wav_to_mp3(test_wav_file)
    mp3_audio = AudioSegment.from_file(io.BytesIO(mp3_data), format="mp3")
    assert int(mp3_audio.duration_seconds) == 33
