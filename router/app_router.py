from fastapi import APIRouter
from pydantic import EmailStr

from core.app_core import create_token, transform_token


router = APIRouter(prefix="/jwt", tags=["JWT AUTH"])


@router.post("/login")
async def login_app(username: str, email: EmailStr):
    return await create_token(username=username, email=email)


@router.post("/decode")
async def decode_app(token: str | bytes):
    return await transform_token(token=token)
