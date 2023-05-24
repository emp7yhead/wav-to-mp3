from fastapi import FastAPI

from app.settings import settings
from app.users.routers import user_router

app = FastAPI()

app.include_router(user_router, prefix=settings.API_VERSION)


@app.get('/')
def index() -> str:
    return 'Welcome to wav-to-mp3. Go to /docs for more information'


@app.get('/ping')
def ping() -> str:
    return 'pong'
