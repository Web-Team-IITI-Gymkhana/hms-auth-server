import uuid

from server.connection import Base
from sqlalchemy import Column, Date, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func


class Staff(Base):
    __tablename__ = "staff"
    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    doctor_uuid = Column(UUID(as_uuid=True), ForeignKey("doctor.uuid"), nullable=False)
    hospital_uuid = Column(UUID(as_uuid=True), ForeignKey("hospital.uuid"), nullable=False)
    position = Column(String(50), nullable=False)
    start_date = Column(Date, nullable=False, server_default=func.now())
    end_date = Column(Date)

    def __repr__(self):
        return str(self.uuid)
