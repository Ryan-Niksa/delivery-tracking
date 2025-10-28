from fastapi import FastAPI
from sqlalchemy import create_engine
from .config import DATABASE_URL

app = FastAPI()

engine = create_engine(DATABASE_URL)

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}
