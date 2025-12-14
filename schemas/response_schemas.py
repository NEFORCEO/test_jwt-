from pydantic import BaseModel, EmailStr

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

