from pydantic import BaseModel, EmailStr
from datetime import datetime

class IndexSchema(BaseModel):
    ping: str 
    time: datetime




class LoginSchema(BaseModel):
    token: str 
    type: str

class DecodeSchema(BaseModel):
    sub: str
    username: str
    email: EmailStr

class MeSchema(BaseModel):
    username: str
    email: EmailStr

class TestSchema(BaseModel):
    result: bool


