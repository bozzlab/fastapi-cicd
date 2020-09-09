#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Peem Srinikorn
# Created Date: Tue Sep  8 20:57:59 +07 2020
# =============================================================================

from fastapi import FastAPI, Header, Cookie, Body, File, UploadFile
from app.db import TSUTAYA_MOVIES, TSUTAYA_MEMBER
from starlette.responses import JSONResponse
from app.helper import generate_id
from pydantic import BaseModel
from enum import Enum
import uvicorn 

class Genre(str, Enum):
    action = "action"
    sci_fi = "sci-fi"
    romantic = "romantic"
    horror = "horror"
    drama = "drama"
    adult = "adult"

class MoviesObject(BaseModel):
    name : str = "Untitled"
    genre : Genre

app = FastAPI( title = "FastAPI Movies Store API",
            description = "Description and technical detail of APIs, Live on Medium",
            version = "1.0.0"
)

@app.get("/movies")
async def fetch_movies(name : str = None):
    if name:
        return {"data" : [TSUTAYA_MOVIES[movie_id] for movie_id in TSUTAYA_MOVIES if TSUTAYA_MOVIES[movie_id]['name'] == name]}

    return {"data" : [TSUTAYA_MOVIES[movie_id] for movie_id in TSUTAYA_MOVIES]}

@app.get("/member")
async def check_member(x_username : str = Header(...)):
    if [ member for member in TSUTAYA_MEMBER if TSUTAYA_MEMBER[member]['name'] == x_username]:
        return {"message" : f"{x_username} is member of TSUTAYA store"}
    else: 
        return {"message" : "Not found"}

@app.get("/member/token")
async def check_token(x_token : str = Cookie(None)):
    if x_token in TSUTAYA_MEMBER.keys():
        return {"message" : f"{TSUTAYA_MEMBER[x_token]['name']} is member of TSUTAYA store and Token is valid"}
    else: 
        return {"message" : "Invalid token"}

@app.post("/movies")
async def insert_movies(req_body : MoviesObject = Body(...), x_username : str = Header(...)):
    # """
    # Insert Movies:
    # - **name**: a title of movies
    # - **genre**: the genre of movies in Genre list

    # Genre List:
    # - ["action", "sci-fi", "romantic", "horror", "drama", "adult"]

    # """
    movie_id = generate_id()
    TSUTAYA_MOVIES.update({ movie_id : {"name" : req_body.name,
                                        "genre" : req_body.genre ,
                                        "created_by" : x_username}})
    return JSONResponse(content = {"message" : f"{req_body.name}, added to TSUTAYA store"}, status_code = 201)

@app.post("/member/profile")
async def insert_image_profile(data : UploadFile = File(...)):
    image = await data.read()
    return {"message" : f"{data.filename}, size {len(image)} bytes, updated to your profile"}

if __name__ == "__main__":
    uvicorn.run("code_for_gist:app", host = "0.0.0.0", port = 8080, debug = True)