from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index() -> str:
    return 'Welcome to wav-to-mp3. Go to /docs for more information'
