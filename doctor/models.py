from server.connection import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID


class Doctor(Base):
    __tablename__ = "doctor"

    uuid = Column(
        UUID(as_uuid=True), ForeignKey("user.uuid"), nullable=False, primary_key=True
    )
    name = Column(String(127), nullable=False)
    degree = Column(String(127), nullable=False)
    medical_profession = Column(String(127), nullable=False)
    experience = Column(Integer, nullable=False)
    phone_number = Column(String(15), nullable=False)
    details_filled = Column(Boolean, nullable=False)
    is_approved = Column(Boolean, nullable=False, default=False)

    def __repr__(self):
        return self.name
