from fastapi import APIRouter
from fastapi.params import Depends
from pydantic import EmailStr

from core.app_core import create_token, transform_token, get_user


router = APIRouter(prefix="/jwt", tags=["JWT AUTH"])


@router.post("/login")
async def login_app(username: str, email: EmailStr):
    return await create_token(username=username, email=email)


@router.post("/decode")
async def decode_app(token: str | bytes):
    return await transform_token(token=token)


@router.get('/me')
async def index_me_app(user = Depends(get_user)):
    return {
        "result": user
    }

@router.post("/test")
async def test_app(username: str, user = Depends(get_user)) -> bool:
    if username == user["username"]:
        return True 
    return False