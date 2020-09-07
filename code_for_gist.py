from fastapi import FastAPI, Header, Body
from app.db import TSUTAYA_MOVIES, TSUTAYA_MEMBER
from pydantic import BaseModel
import uvicorn 

class MoviesObject(BaseModel):
    name : str 
    genre : Genre

app = FastAPI()

@app.get("/movies")
async def fetch_movies(name : str = None):
    if name:
        return {"data" : [TSUTAYA_MOVIES[movie_id] for movie_id in TSUTAYA_MOVIES if TSUTAYA_MOVIES[movie_id]['name'] == name]}

    return {"data" : [TSUTAYA_MOVIES[movie_id] for movie_id in TSUTAYA_MOVIES]}

@app.get("/member")
async def check_member(x_username : str = Header(...)):
    if [TSUTAYA_MEMBER[member] for member in TSUTAYA_MEMBER if TSUTAYA_MEMBER[member]['name'] == x_username]:
        return {"message" : f"{x_username} is member of TSUTAYA store"}
    else: 
        return {"message" : "Not found"}

app.post("/movies")
async def insert_movies(req_body : MoviesObject = Body(...)):
    pass

if __name__ == "__main__":
    uvicorn.run("code_for_gist:app", host = "0.0.0.0", port = 8080, debug = True)