from sqlalchemy.orm import Session

from schemas.teacher import TeacherCreate, TeacherUpdate
from db.models.teacher import Teacher


def create_new_teacher(teacher: TeacherCreate, db: Session):
    teacher = Teacher(
        names=teacher.names,
        lastnames=teacher.lastnames
    )
    db.add(teacher)
    db.commit()
    db.refresh(teacher)
    return teacher


def retrieve_teacher(id: int, db: Session):
    teacher = db.query(Teacher).filter(Teacher.id_teacher == id).first()
    return teacher


def list_teachers(db: Session):
    teachers = db.query(Teacher).all()
    return teachers


def update_existing_teacher(id: int, teacher: TeacherUpdate, db: Session):
    teacher_in_db = retrieve_teacher(id=id, db=db)
    if not teacher_in_db:
        return
    teacher_data = teacher.dict(exclude_unset=True)
    for key, value in teacher_data.items():
        setattr(teacher_in_db, key, value)
    db.add(teacher_in_db)
    db.commit()
    db.refresh(teacher_in_db)
    return teacher_in_db


def delete_teacher(id: int, db: Session):
    teacher_in_db = db.query(Teacher).filter(Teacher.id_teacher == id)
    if not teacher_in_db.first():
        return {"error": f"Could not find teacher with id {id}"}
    teacher_in_db.delete()
    db.commit()
    return {"msg": f"deleted teacher with id {id}"}
