from fastapi import APIRouter
from api.routes import route_teacher
from api.routes import route_course

api_router = APIRouter()
api_router.include_router(route_teacher.router, prefix="", tags=["teachers"])
api_router.include_router(route_course.router, prefix="", tags=["courses"])