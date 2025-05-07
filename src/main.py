from fastapi import FastAPI
import uvicorn

from src.routes.auth import auth_router
from src.routes.book import book_router
from contextlib import asynccontextmanager
from src.config.db import init_db
from src.config.example import create_tables


@asynccontextmanager
async def life_session(app: FastAPI):
    print('Server is running')
    await init_db()
    yield
    print('Server stopped')


app = FastAPI(
    title='Book API',
    description='Book API',
    version='1.0',
    lifespan=life_session
)
app.include_router(book_router, prefix="/books", tags=["books"])
app.include_router(auth_router, prefix="/auth", tags=["auth"])


@app.get("/")
async def home():
    return {'message': 'Hello World'}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8002, reload=True)
