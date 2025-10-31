from sqlalchemy import Column, Integer, String, DateTime, func
from backend.core.database import Base

class HR(Base):
    __tablename__ = "hrs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(128), nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    phone = Column(String(32), nullable=True)
    created_at = Column(DateTime, server_default=func.now())
