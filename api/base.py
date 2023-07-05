from fastapi import APIRouter
from api.routes import route_teacher

api_router = APIRouter()
api_router.include_router(route_teacher.router, prefix="", tags=["teachers"])
