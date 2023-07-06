from sqlalchemy.orm import Session

from schemas.course import CourseCreate, CourseUpdate
from db.models.course import Course

def create_new_course(course: CourseCreate, db: Session):
    
    course = Course(course_name = course.course_name, id_course_type = course.id_course_type)
    
    db.add(course)
    db.commit()
    db.refresh(course)
    return course

def retrieve_course(id: int, db: Session):
    course = db.query(Course).filter(Course.id_course == id).first()
    return course

def list_courses (db: Session):
    courses = db.query(Course).all()
    return courses

def update_existing_course(id: int, course: CourseUpdate, db: Session):
    course_in_db = retrieve_course(id=id, db=db)
    if not course_in_db:
        return
    course_data = course.dict(exclude_unset=True)
    for key, value in course_data.items():
        setattr(course_in_db, key, value)
    db.add(course_in_db)
    db.commit()
    db.refresh(course_in_db)
    return course_in_db

def delete_course(id: int, db: Session):
    course_in_db = db.query(Course).filter(Course.id_course == id)
    if not course_in_db.first():
        return {'error': f'Could not find course with id {id}'}
    course_in_db.delete()
    return {'msg': f'deleted course with id {id}'}

