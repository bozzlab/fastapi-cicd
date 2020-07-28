from fastapi.testclient import TestClient
from main import app
import json
import logging

client = TestClient(app)

member_chlid = None
member_mature = None

def test_register_member_child():
    response = client.post("/api/v1/member", 
                json = {"name" : "Henry", "age" : 12, "phone_number" : "1234"}) 
    global member_chlid
    member_chlid = response.json()['message']
    assert response.status_code == 201
    assert isinstance(response.json()['card_id'], str)
    assert len(response.json()['card_id']) == 8

def test_register_member_mature():
    response = client.post("/api/v1/member", 
                json = {"name" : "Nesta", "age" : 22, "phone_number" : "4321"}) 
    global member_chlid
    member_mature = response.json()['message']
    assert response.status_code == 201
    assert isinstance(response.json()['card_id'], str)
    assert len(response.json()['card_id']) == 8