from fastapi import FastAPI, Depends, Header, HTTPException, Response, APIRouter
from config import database

router = APIRouter()
db = database

@router.get("/movies")
async def list_movies():
    return await db.fetch_all("SELECT * FROM movies")
