import jwt
from config import settings


async def encode_token(
    payload: dict,
    private_key: str = settings.config.private_key,
    algorithm: str = settings.config.algoritm,
):
    encode_token = jwt.encode(payload=payload, key=private_key, algorithm=algorithm)
    return encode_token


async def decoded_token(
    token: str | bytes,
    private_key: str = settings.config.private_key,
    algorithm: str = settings.config.algoritm,
):
    decode_token = jwt.decode(jwt=token, key=private_key, algorithms=[algorithm])
    return decode_token
