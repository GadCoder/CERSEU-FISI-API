from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends
from fastapi import HTTPException, status
from schemas.course_type import CourseTypeCreate, CourseTypeUpdate
from db.session import get_db
from db.repository.course_type import create_new_course_type, retrieve_course_type, list_course_types, update_existing_course_type, delete_course_type

router = APIRouter()

@router.post("/create-course-type/")
def create_course_type(course_type: CourseTypeCreate, db: Session = Depends(get_db)):
    course_type = create_new_course_type(course_type = course_type, db = db)
    return course_type

@router.get("/get-course-type/{id}")
def get_course_type(id: int, db: Session = Depends(get_db)):
    course_type = retrieve_course_type(id=id, db=db)
    if not course_type:
        raise HTTPException(
            detail=f'course type type with ID {id} does not exist', status_code=status.HTTP_404_NOT_FOUND
        )
    return course_type

@router.get("/get-all-course-types")
def get_all_course_types(db: Session = Depends(get_db)):
    course_types = list_course_types(db=db)
    return course_types

@router.patch("/update-course-type/{id}")
def update_course_type (id: int, course_type: CourseTypeUpdate, db: Session = Depends(get_db)):
    course_type = update_existing_course_type(id=id, course_type=course_type, db=db)
    if not course_type:
        raise HTTPException(
            detail=f'course type with ID {id} does not exist', status_code=status.HTTP_404_NOT_FOUND
        )
    return course_type

@router.delete("/delete-course-type/{id}")
def delete_a_course_type(id: int, db: Session = Depends(get_db)):
    message = delete_course_type(id=id, db=db)
    if message.get("error"):
        raise HTTPException(detail=message.get("error"),
                            status_code=status.HTTP_400_BAD_REQUEST)
    return {"msg": f"Successfully deleted course type with id {id}"}