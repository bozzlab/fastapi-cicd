from fastapi import FastAPI, Depends, Header, HTTPException, Response
from .db import TSUTAYA_MEMBER
from .api import movies, member
import logging

app = FastAPI(title = "FastAPI Tsutaya Video Store",
              version = "0.0.1")

@app.get("/api/v1/info")
async def information():
    return {"app_name": app.title , "version" : app.version, "documents_path" : "/docs"}

@app.on_event("startup")
async def startup_event():
    logging.info("Application start")

@app.on_event("shutdown")
async def shutdown_event():
    logging.info("Application shutdown")

async def get_x_card_id_token(x_card_id: str = Header(...)):
    try:
        if not TSUTAYA_MEMBER.get(x_card_id, False):
            raise HTTPException(status_code = 400, detail = "X-Card-ID header invalid")
    except Exception as e:
        logging.error(e)
        raise HTTPException(status_code = 400, detail = "X-Card-ID header invalid")


app.include_router(
    member.router,
    prefix="/api/v1",
    tags=["member"],
    responses={404: {"message": "Not found"}},
)

app.include_router(
    movies.router,
    prefix="/api/v1",
    tags=["movies"],
    dependencies=[Depends(get_x_card_id_token)],
    responses={404: {"message": "Not found"}},
)
