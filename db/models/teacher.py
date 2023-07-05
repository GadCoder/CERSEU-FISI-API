from sqlalchemy import Boolean, Column, Integer, String
from db.session import Base


class Teacher(Base):
    __tablename__ = "teacher"

    id_teacher = Column(Integer, primary_key=True,
                        index=True, autoincrement=True)
    names = Column(String)
    lastnames = Column(String)
    is_available = Column(Boolean, default=True)
    photo_url = Column(String)
