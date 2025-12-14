from fastapi import APIRouter
from fastapi.params import Depends
from pydantic import EmailStr

from schemas.depends_schemas import UserResponse, TestResponse
from schemas.response_schemas import LoginSchema, DecodeSchema, MeSchema, TestSchema

from core.app_core import create_token, transform_token, get_user

router = APIRouter(prefix="/jwt", tags=["JWT AUTH"])


@router.post("/login", response_model=LoginSchema)
async def login_app(username: str, email: EmailStr):
    return await create_token(username=username, email=email)


@router.post("/decode", response_model=DecodeSchema)
async def decode_app(token: str | bytes):
    return await transform_token(token=token)


@router.get('/me', response_model=MeSchema)
async def index_me_app(user: UserResponse = Depends(get_user)):
    return {
        "username": user["username"],
        "email": user["email"]
    }

@router.post("/test", response_model=TestSchema)
async def test_app(username: str, user: TestResponse  = Depends(get_user)) -> dict[str, bool]:
    if username == user["username"]:
        return {"result": True} 
    return {"result": False}