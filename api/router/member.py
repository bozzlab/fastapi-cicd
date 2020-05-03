from fastapi import FastAPI, Header, APIRouter, Body, Response
from config import database
import logging

router = APIRouter()
db = database

@router.post("/member")
async def register(response: Response, body : dict = Body(...)):
    query_statement = "INSERT INTO member (name, age, id_card, phone_number, \
                        created_at) VALUES (:name, :age, :id_card,\
                        :phone_number, NOW())"
    values = {"name" :body['name'], "age" : body['age'], \
            "id_card" : body['id_card'], "phone_number" : body['phone_number']}
    try:
        import pdb; pdb.set_trace()
        result = await db.execute(query = query_statement, values = values)
        # response.set_cookie(key="fakesession", value="fake-cookie-session-value")
        logging.info(result)
        return {"status" : "success"}
    except Exception as e:
        return {"status" : "failed", "error_msg" : str(e)}

