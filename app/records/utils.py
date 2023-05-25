from fastapi import UploadFile
from pydub import AudioSegment


def convert_wav_to_mp3(wav_file: UploadFile):
    mp3_data = AudioSegment.from_wav(wav_file.file).export(format="mp3").read()
    return mp3_data
