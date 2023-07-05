from pydantic import BaseModel
from typing import Optional


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


class TeacherUpdate(BaseModel):
    names: Optional[str] = None
    lastnames: Optional[str] = None
    is_available: Optional[bool] = None
    photo_url: Optional[str] = None
