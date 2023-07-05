from sqlalchemy import Column, Integer, String, ForeignKey
from db.session import Base


class Course(Base):
    __tablename__ = "course"

    id_course = Column(Integer, primary_key=True,
                       index=True, autoincrement=True)
    course_name = Column(String)

    id_teacher = Column(Integer, ForeignKey("teacher.id_teacher"))
    id_course_type = Column(Integer, ForeignKey("course_type.id_course_type"))
