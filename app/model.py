from pydantic import BaseModel

class RegisterObject(BaseModel):
    name : str 
    age : int
    phone_number : str