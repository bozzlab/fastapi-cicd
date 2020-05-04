from fastapi import FastAPI, APIRouter, Body, Response
from config import database
import logging

router = APIRouter()
db = database

@router.post("/member")
async def register(response: Response, body : dict = Body(...)):
    insert_query = "INSERT INTO member (name, age, id_card, phone_number, \
                        created_at) VALUES (:name, :age, :id_card,\
                        :phone_number, NOW())"
    values = {"name" :body['name'], "age" : body['age'], \
            "id_card" : body['id_card'], "phone_number" : body['phone_number']}
    select_id_query = "SELECT id, age, is_borrow FROM member \
                        WHERE id_card = :id_card"
    try:
        await db.execute(query = insert_query, values = values)
        unique_key = await db.fetch_one(query = select_id_query, 
                                        values = {"id_card" : body['id_card']})
        response.set_cookie(key = "tsutaya-user", value = unique_key['id'],
                            expires = 3600)
        response.set_cookie(key = "tsutaya-age", value = unique_key['age'],
                            expires = 3600)
        return {"status" : "success", "error_code" : 0}
    except Exception as e:
        logging.error(str(e))
        return {"status" : "failed" , "error_code" : 1}