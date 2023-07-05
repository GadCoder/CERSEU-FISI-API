from pydantic import BaseModel
from typing import Optional


class CourseBase(BaseModel):
    course_name: str


class CourseCreate(CourseBase):
    pass


class Course(CourseBase):
    id_course: int
    id_teacher: Optional[int]
    id_course_type: int

    class Config:
        orm_mode = True
