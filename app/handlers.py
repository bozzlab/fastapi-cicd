from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()

db_connector = {}

@app.get("/api/v1/echo")
def echo_testcheck():
    return {"Hello" : "World"}

@app.get("/api/v1/mongo")
def mongodb_testcheck():
    return {"mongodb" : db_connector['mongo'].list_database_names() }

@app.get("/api/v1/mongo_check")
def db_testcheck():
    data = db_connector['mongo']
    col = data['movies']
    return {"mongodb" : col['movies'].find_one()['username'] }

@app.on_event("startup")
async def startup_event():
    db_connector['mongo'] = MongoClient("mongodb://fastapi-admin:fastapi-password@0.0.0.0:27017")
