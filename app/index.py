
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from datetime import datetime

async def index_app(app: FastAPI) -> None:
    @app.get('/')
    async def index():
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "ping": "pong",
                "time": datetime.utcnow().isoformat(),
            }
        )