from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import ResponseValidationError
from fastapi.exceptions import RequestValidationError


async def handler_app(app: FastAPI) -> None:

    @app.exception_handler(RequestValidationError)
    async def request_handler(
        request: Request,
        exc: RequestValidationError,
    ):
        return JSONResponse(
            status_code=status.HTTP_418_IM_A_TEAPOT,
            content={"name": exc.args, "message": "Opps error app"},
        )

    @app.exception_handler(ResponseValidationError)
    async def response_handler(request: Request,exc: ResponseValidationError):
        return JSONResponse(
            status_code=status.HTTP_418_IM_A_TEAPOT,
            content={
                "name": exc.endpoint_path,
                "message": "Opps error app, sorry user",
            },
        )
    
