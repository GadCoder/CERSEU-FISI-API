from fastapi import APIRouter, Request
from sqlalchemy.orm import Session
from db.session import get_db
from fastapi import Depends

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from db.repository.teacher import list_teachers
from db.repository.course import list_courses

templates = Jinja2Templates(directory="templates")
general_pages_router = APIRouter()


@general_pages_router.get("/")
async def home(request: Request):
    return templates.TemplateResponse("pages/homepage.html", {"request": request})


@general_pages_router.get("/adminpage")
async def home(request: Request, db: Session = Depends(get_db)):
    teachers_data = list_teachers(db=db)
    courses_data = list_courses(db=db)
    return templates.TemplateResponse("pages/adminpage.html", {"request": request, "teacher_data": teachers_data, "courses_data": courses_data})
