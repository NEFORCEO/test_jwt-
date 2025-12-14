from router.app_router import router

from fastapi import APIRouter

app_router = APIRouter()
app_router.include_router(router=router)
