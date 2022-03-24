from server.connection import Base
from sqlalchemy import Boolean, Column, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID



class Hospital(Base):
    __tablename__ = "hospital"

    name = Column(String(127), nullable=False)
    uuid = Column(
        UUID(as_uuid=True), ForeignKey("user.uuid"), nullable=False, primary_key=True
    )
    address = Column(String(255), nullable=False)
    phone_number = Column(String(15), nullable=False)
    details_filled = Column(Boolean, nullable=False)
    is_approved = Column(Boolean, nullable=False, default=False)
    # meta_data = Column(JSON)

    def __repr__(self):
        return self.name

