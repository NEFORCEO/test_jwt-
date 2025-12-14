from fastapi import FastAPI
from router import app_router

async def routers_app(app: FastAPI):
    app.include_router(router=app_router)