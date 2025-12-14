from datetime import datetime


from fastapi import FastAPI, status
from fastapi.responses import JSONResponse

from schemas.response_schemas import IndexSchema


async def index_app(app: FastAPI) -> None:
    @app.get('/', tags=["INDEX APP"], response_model=IndexSchema)
    async def index() -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "ping": "pong",
                "time": datetime.utcnow().isoformat(),
            }
        )