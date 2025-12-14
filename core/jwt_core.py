import jwt
from config import settings


async def encoded_token(
    payload: dict,
    private_key: str | None = settings.config.private_key,
    algorithm: str | None  = settings.config.algorithm,
):
    encode_token = jwt.encode(payload=payload, key=private_key, algorithm=algorithm)
    return encode_token


async def decoded_token(
    token: str | bytes,
    private_key: str | None = settings.config.private_key,
    algorithm: str | None = settings.config.algorithm,
):
    decode_token = jwt.decode(jwt=token, key=private_key, algorithms=[algorithm])
    return decode_token
