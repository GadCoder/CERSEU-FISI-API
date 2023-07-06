from sqlalchemy.orm import Session

from schemas.course_type import CourseTypeCreate, CourseTypeUpdate
from db.models.course_type import CourseType

def create_new_course_type(course_type: CourseTypeCreate, db: Session):
    course_type = CourseType(course_type = course_type.course_type)
    db.add(course_type)
    db.commit()
    db.refresh(course_type)
    return course_type

def retrieve_course_type(id: int, db: Session):
    course_type = db.query(CourseType).filter(CourseType.id_course_type==id).first()
    return course_type

def list_course_types(db:Session):
    course_types = db.query(CourseType).all()
    return course_types

def update_existing_course_type(id: int, course_type: CourseTypeUpdate, db: Session):
    course_type_in_db = retrieve_course_type(id=id, db=db)
    if not course_type_in_db:
        return
    course_type_data = course_type.dict(exclude_unset=True)
    for key, value in course_type_data.items():
        setattr(course_type_in_db, key, value)
    db.add(course_type_in_db)
    db.commit()
    db.refresh(course_type_in_db)
    return course_type_in_db

def delete_course_type(id: int, db:Session):
    course_type_in_db = db.query(CourseType).filter(CourseType.id_course == id)
    if not course_type_in_db.first():
        return {'error': f'Could not find course type with id {id}'}
    course_type_in_db.delete()
    return {'msg': f'deleted course type with id {id}'}