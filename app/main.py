from fastapi import FastAPI

from app.routers import base_router
from app.settings import settings

app = FastAPI()

app.include_router(base_router, prefix=settings.API_VERSION)


@app.get('/')
def index() -> str:
    return 'Welcome to wav-to-mp3. Go to /docs for more information'


@app.get('/ping')
def ping() -> str:
    return 'pong'
