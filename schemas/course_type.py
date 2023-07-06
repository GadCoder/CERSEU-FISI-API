from pydantic import BaseModel
from typing import Optional

class CourseTypeBase(BaseModel):
    pass


class CourseTypeCreate(BaseModel):
    course_type: str


class CourseType(CourseTypeBase):
    id_course_type: int

    class Config:
        orm_mode = True

class CourseTypeUpdate(BaseModel):
    course_type: Optional[str] = None