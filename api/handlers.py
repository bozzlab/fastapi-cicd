from fastapi import FastAPI, Depends, Header, HTTPException, Response
from .router import movies, member, borrow
from config import database

app = FastAPI(title = "FastAPI-Movies",
              version = "0.0.1",
              openapi_prefix="/api/v1")

@app.get("/api/v1/info")
async def information():
    return {"app_name": app.title , "version" : app.version, "documents_path" : "/docs"}

@app.on_event("startup")
async def startup_event():
    await database.connect()    

@app.on_event("shutdown")
async def shutdown_event():
    await database.disconnect()

async def get_token_header(x_token: str = Header(...)):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")

app.include_router(
    member.router,
    prefix="/api/v1",
    tags=["member"],
    responses={404: {"description": "Not found"}},
)

app.include_router(
    movies.router,
    prefix="/api/v1",
    tags=["movies"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

app.include_router(
    borrow.router,
    prefix="/api/v1",
    tags=["borrow"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)