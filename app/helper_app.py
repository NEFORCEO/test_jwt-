from fastapi import FastAPI
from .routers_app import routers_app
from .app_error import handler_app


async def hellper_app(app: FastAPI) -> None:
    await routers_app(app=app)
    await handler_app(app=app)
