from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI

from .helper_app import hellper_app


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator:
    print("RUN APP")
    await hellper_app(app=app)
    yield
    print("CLOSE APP")
