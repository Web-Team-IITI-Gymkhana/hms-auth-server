from server.connection import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID


class Patient(Base):
    __tablename__ = "patient"
    nhid = Column(Integer, primary_key=True)
    uuid = Column(UUID(as_uuid=True), ForeignKey("user.uuid"), nullable=False)
    name = Column(String(127), nullable=False)
    gender = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    address = Column(String(255), nullable=False)
    # meta_data = Column(JSON)
    details_filled = Column(Boolean, nullable=False)

    def __repr__(self):
        return self.nhid
