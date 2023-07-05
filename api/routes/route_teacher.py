from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends
from fastapi import HTTPException, status
from schemas.teacher import TeacherCreate, TeacherUpdate
from db.session import get_db
from db.repository.teacher import create_new_teacher, retrieve_teacher, list_teachers, update_existing_teacher, delete_teacher


router = APIRouter()


@router.post("/create-teacher/")
def create_teacher(teacher: TeacherCreate, db: Session = Depends(get_db)):
    teacher = create_new_teacher(teacher=teacher, db=db)
    return teacher


@router.get("/get-teacher/{id}")
def get_teacher(id: int, db: Session = Depends(get_db)):
    teacher = retrieve_teacher(id=id, db=db)
    if not teacher:
        raise HTTPException(
            detail=f"Teacher with ID {id} does not exist.", status_code=status.HTTP_404_NOT_FOUND)
    return teacher


@router.get("/get-all-teachers/")
def get_all_teachers(db: Session = Depends(get_db)):
    teachers = list_teachers(db=db)
    return teachers


@router.patch("/update-teacher/{id}")
def update_teacher(id: int, teacher: TeacherUpdate, db: Session = Depends(get_db)):
    teacher = update_existing_teacher(id=id, teacher=teacher, db=db)
    if not teacher:
        raise HTTPException(
            detail=f"Teacher with ID {id} does not exist.", status_code=status.HTTP_404_NOT_FOUND)
    return teacher


@router.delete("/delete-teacher/{id}")
def delete_a_teacher(id: int, db: Session = Depends(get_db)):
    message = delete_teacher(id=id, db=db)
    if message.get("error"):
        raise HTTPException(detail=message.get("error"),
                            status_code=status.HTTP_400_BAD_REQUEST)
    return {"msg": f"Successfully deleted teacher with id {id}"}
