from fastapi import FastAPI

from .lifespan import lifespan


def create_app() -> FastAPI:
    app = FastAPI(lifespan=lifespan)
    return app
