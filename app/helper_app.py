import asyncio

from fastapi import FastAPI
from .routers_app import routers_app
from .app_error import handler_app
from .index import index_app


async def hellper_app(app: FastAPI) -> None:
     await asyncio.gather(
          index_app(app=app),
          routers_app(app=app),
          handler_app(app=app),
     )
