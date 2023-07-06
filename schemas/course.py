from pydantic import BaseModel
from typing import Optional


class CourseBase(BaseModel):
    course_name: str
    id_course_type: int


class CourseCreate(CourseBase):
    pass


class Course(CourseBase):
    id_course: int
    id_teacher: Optional[int]
    id_course_type: int

    class Config:
        orm_mode = True
        
class CourseUpdate(BaseModel):
    course_name: Optional[str] = None
    id_course_type: Optional[int] = None
