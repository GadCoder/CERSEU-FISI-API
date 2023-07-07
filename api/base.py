from fastapi import APIRouter
from api.routes import route_teacher
from api.routes import route_course
from api.routes import route_course_type
from api.routes import route_homepage

api_router = APIRouter()
api_router.include_router(route_teacher.router, prefix="", tags=["teachers"])
api_router.include_router(route_course.router, prefix="", tags=["courses"])
api_router.include_router(route_course_type.router,
                          prefix="", tags=["courses types"])

api_router.include_router(route_homepage.general_pages_router)
