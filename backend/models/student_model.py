from sqlalchemy import Column, Integer, String, Float, DateTime, func
from backend.core.database import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(128), nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    department = Column(String(128), nullable=True)
    year_of_study = Column(Integer, nullable=True)
    cgpa = Column(Float, nullable=True)
    resume_link = Column(String(512), nullable=True)
    created_at = Column(DateTime, server_default=func.now())
