from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends
from fastapi import HTTPException, status
from schemas.course import CourseCreate, CourseUpdate
from db.session import get_db
from db.repository.course import create_new_course, retrieve_course, list_courses, update_existing_course, delete_course

router = APIRouter()

@router.post("/create-course/")
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    course = create_new_course(course = course, db = db)
    return course

@router.get("/get-course/{id}")
def get_course(id: int, db: Session = Depends(get_db)):
    course = retrieve_course(id=id, db=db)
    if not course:
        raise HTTPException(
            detail=f'Course with ID {id} does not exist', status_code=status.HTTP_404_NOT_FOUND
        )
    return course

@router.get("/get-all-courses")
def get_all_courses(db: Session = Depends(get_db)):
    courses = list_courses(db=db)
    return courses

@router.patch("/update.course/{id}")
def update_course (id: int, course: CourseUpdate, db: Session = Depends(get_db)):
    course = update_existing_course(id=id, course=course, db=db)
    if not course:
        raise HTTPException(
            detail=f'Course with ID {id} does not exist', status_code=status.HTTP_404_NOT_FOUND
        )
    return course

@router.delete("/delete-course/{id}")
def delete_a_course(id: int, db: Session = Depends(get_db)):
    message = delete_course(id=id, db=db)
    if message.get("error"):
        raise HTTPException(detail=message.get("error"),
                            status_code=status.HTTP_400_BAD_REQUEST)
    return {"msg": f"Successfully deleted course with id {id}"}