from pydantic import BaseModel


class CourseTypeBase(BaseModel):
    pass


class CourseTypeCreate(BaseModel):
    course_type: str


class CourseType(CourseTypeBase):
    id_course_type: int

    class Config:
        orm_mode = True
