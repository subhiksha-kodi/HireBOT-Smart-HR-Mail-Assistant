from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from backend.core.database import Base


class MailLog(Base):
    __tablename__ = "mail_logs"

    id = Column(Integer, primary_key=True, index=True)
    subject = Column(String(255), nullable=False)
    body = Column(Text, nullable=True)
    recipient_email = Column(String(255), nullable=False)
    status = Column(String(50), nullable=False, default="pending")  # pending, sent, failed
    sent_at = Column(DateTime, server_default=func.now())

    hr_id = Column(Integer, ForeignKey("hrs.id", ondelete="SET NULL"), nullable=True)

    # Relationship — each mail log optionally belongs to an HR
    hr = relationship("HR", backref="mail_logs")
