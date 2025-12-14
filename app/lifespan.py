from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.helper_app import hellper_app


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("RUN APP")
    await hellper_app(app=app)
    yield
    print("CLOSE APP")
