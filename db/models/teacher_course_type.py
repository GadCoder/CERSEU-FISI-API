from sqlalchemy import Column, ForeignKey, Integer
from db.session import Base


class TeacherCourseType(Base):
    __tablename__ = "teacher_course_type"

    id = Column(Integer, primary_key=True,
                index=True, autoincrement=True)
    id_teacher = Column(Integer, ForeignKey("teacher.id_teacher"))
    id_course_type = Column(Integer, ForeignKey("course_type.id_course_type"))
