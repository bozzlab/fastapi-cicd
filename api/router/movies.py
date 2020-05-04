from fastapi import FastAPI, Cookie, Response, APIRouter
from config import database

router = APIRouter()
db = database

@router.get("/movies")
async def all_movies(genre: str, name: str, id: int):
    try:
        list_movies =  await db.fetch_all("SELECT * FROM movies")
        return
    except Exception as e:
        logging.error(str(e))
        return {"status" : "failed" , "error_code" : 1}
