from core.jwt_core import decoded_token, encoded_token
from pydantic import EmailStr
import random
from fastapi.responses import JSONResponse
from fastapi import status



async def create_token(username: str, email: EmailStr) -> JSONResponse:
    response = await encoded_token(payload={
        "sub": str(random.randint(100000, 999999)),
        "username": username,
        "email": email
    })
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "token": response,
            "type": "Bearer"
        }
    )


async def transform_token(token: str | bytes) -> JSONResponse:
    response = await decoded_token(token=token)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "result": response
        }
    )