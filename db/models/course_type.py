from sqlalchemy import Column,  Integer, String
from db.session import Base


class CourseType(Base):
    __tablename__ = "course_type"

    id_course_type = Column(Integer, primary_key=True,
                            index=True, autoincrement=True)
    course_type = Column(String)
