from starlette.responses import JSONResponse
from fastapi import FastAPI, Header, Response, APIRouter, Body
from app.db import TSUTAYA_MOVIES, TSUTAYA_MEMBER
from app.helper import is_adult, generate_id
from app.model import MoviesObject, RemoveMoviesObject
import logging

router = APIRouter()

@router.get("/movies", status_code = 200)
async def all_movies(x_card_id : str = Header(...)) -> Response:
    try:
        if is_adult(x_card_id):
            return {"data" : [TSUTAYA_MOVIES[movie_id] for movie_id in TSUTAYA_MOVIES]}
        else:
            return {"data" : [TSUTAYA_MOVIES[movie_id] for movie_id in TSUTAYA_MOVIES if TSUTAYA_MOVIES[movie_id]['genre'] != "adult"]}

    except Exception as e:
        logging.error(e)
        return JSONResponse(content = {"message" : "Error"}, status_code = 400)

@router.get("/movies/list_genre", status_code = 200)
async def genre_movies(x_card_id : str = Header(...), genre : str = None) -> Response:
    try:
        if not genre:
            return {"data" : set([TSUTAYA_MOVIES[movie_id]['genre'] for movie_id in TSUTAYA_MOVIES])}
        
        if not is_adult(x_card_id):
            if genre == "adult" :
                return JSONResponse(content = {"message" : "You cannot get adult video."}, status_code = 403) 
        
        return {"data" : [TSUTAYA_MOVIES[movie_id] for movie_id in TSUTAYA_MOVIES if TSUTAYA_MOVIES[movie_id]['genre'] == genre]}

    except Exception as e:
        logging.error(e)
        return JSONResponse(content = {"message" : "Error"}, status_code = 400)

@router.post("/movies", status_code = 201)
async def insert_new_movies(x_card_id : str = Header(...), req_body : MoviesObject = Body(...)) -> Response:
    try:
        if not req_body:
            return {"message" : "Invalid Requests"}
            
        movie_id = generate_id()

        if not is_adult(x_card_id):
            if req_body.genre == "adult":
                return JSONResponse(content = {"message" : "You cannot insert this movie."}, status_code = 400)   
            
        TSUTAYA_MOVIES.update({ movie_id : {"name" : req_body.name,
                                            "genre" : req_body.genre ,
                                            "created_by" : TSUTAYA_MEMBER[x_card_id]['name'],
                                            "is_available" : True,
                                            "borrower" : None}})

        return {"message" : f"{req_body.name} has been added", "movie_id" : movie_id}

    except Exception as e:
        logging.error(e)
        return JSONResponse(content = {"message" : "Error"}, status_code = 400)            

@router.delete("/movies", status_code = 200)
async def delete_movie(x_card_id : str = Header(...), req_body : RemoveMoviesObject = Body(...)) -> Response:
    try:
        if not req_body:
            return {"message" : "Invalid Requests"}
        
        if not TSUTAYA_MOVIES.get(req_body.movie_id, False):
            return JSONResponse(content = {"message" : "Movie not found."}, status_code = 400)        
        
        if TSUTAYA_MOVIES[req_body.movie_id]['created_by'] == TSUTAYA_MEMBER[x_card_id]['name']:
            TSUTAYA_MOVIES.pop(req_body.movie_id)
            return {"message" : f"{req_body.name} has been removed"}
        else: 
            return {"message" : "You cannot remove this item."}

    except Exception as e:
        logging.error(e)
        return JSONResponse(content = {"message" : "Error"}, status_code = 400)    