#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Peem Srinikorn
# Created Date: Tue Sep  8 20:57:59 +07 2020
# =============================================================================

from starlette.responses import JSONResponse
from fastapi import FastAPI, APIRouter, Body, Response
from app.db import TSUTAYA_MEMBER
from app.model import RegisterObject
from app.helper import generate_id
import logging

router = APIRouter()

@router.post("/member", status_code = 201)
async def register(req_body : RegisterObject = Body(...)) -> Response:
    try:
        if req_body:
            card_id = generate_id()
            TSUTAYA_MEMBER.update({card_id : {"name" : req_body.name, 
                                            "age" : req_body.age, 
                                            "phone_number" : req_body.phone_number, 
                                            "role" : "member"}})
            return {"card_id" : card_id}
        else: 
            return {"message" : "Invalid Requests"}
    except Exception as e:
        logging.error(e)
        return JSONResponse(content = {"message" : "Error"}, status_code = 400)
        
@router.get("/member", status_code = 200)
async def register(card_id : str) -> Response:
    try:
        if card_id:
            if TSUTAYA_MEMBER.get(card_id, False):
                return {"data" : [TSUTAYA_MEMBER[card_id]]}
            else: 
                return {"data" : "Not found"}
        else: 
            return {"message" : "Invalid Requests"}
    except Exception as e:
        logging.error(e)
        return JSONResponse(content = {"message" : "Error"}, status_code = 400)