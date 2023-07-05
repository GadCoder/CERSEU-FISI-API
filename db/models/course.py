from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.session import Base


class Course(Base):
    __tablename__ = "course"

    id_course = Column(Integer, primary_key=True,
                       index=True, autoincrement=True)
    course_name = Column(String)
    id_teacher = relationship("Teacher", back_populates="id_teacher")
    id_course_type = relationship(
        "CourseType", back_populates="id_course_type")
