from pydantic import BaseModel


class TeacherBase(BaseModel):
    names: str
    lastnames: str


class TeacherCreate(TeacherBase):
    pass


class Teacher(TeacherBase):
    id_teacher: int
    is_available: bool
    photo_url: str

    class Config:
        orm_mode = True
