import uuid

from server.connection import Base
from sqlalchemy import Boolean, Column, String
from sqlalchemy.dialects.postgresql import UUID


class User(Base):
    __tablename__ = "user"

    """Ideally, mobile numbers should be used to signup users, because a larger fraction of people do not have access to emails.
    But, using OTP as a service would have been costly to us, thus we used email to set an example of how this would work."""

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    email = Column(String(127), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    is_verified = Column(Boolean, nullable=False)
    role = Column(String(25), nullable=False)

    def __repr__(self):
        return self.email


class Blacklisted_Token(Base):
    __tablename__ = "blacklisted_token"
    token = Column(String, primary_key=True)
