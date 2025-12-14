from pydantic import BaseModel, EmailStr

class UserResponse(BaseModel):
    username: str
    email: EmailStr

class TestResponse(BaseModel):
    username: str