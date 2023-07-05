from pydantic import BaseModel


class TeacherCourseTypeBase(BaseModel):
    pass


class TeacherCourseTypeCreate(TeacherCourseTypeBase):
    id_teacher: int
    id_course_type: int


class TeacherCourseType(TeacherCourseTypeBase):
    id: int

    class Config:
        orm_mode = True
