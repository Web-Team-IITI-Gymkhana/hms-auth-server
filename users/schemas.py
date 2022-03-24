from enum import Enum
from typing import Optional
from pydantic import BaseModel, EmailStr, UUID4


class Gender(Enum):
    male = "male"
    female = "female"
    other = "other"


class Roles(Enum):
    patient = "patient"
    doctor = "doctor"
    hospital = "hospital"


class Token(BaseModel):
    access_token: str


class TokenData(BaseModel):
    uuid: Optional[UUID4] = None


class UserCredentials(BaseModel):
    email: EmailStr
    password: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "email": "anonymous@xyz.com",
                "password": "d1e8a70b5ccab1dc2f56bbf7e99f064a660c08e361a35751b9c483c88943d082",
            }
        }


class UserId(UserCredentials):
    role: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "email": "anonymous@xyz.com",
                "password": "d1e8a70b5ccab1dc2f56bbf7e99f064a660c08e361a35751b9c483c88943d082",
                "role": "patient",
            }
        }


class User_Schema(UserId):
    uuid: UUID4
    is_verified: bool

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "uuid": "2996377c-020a-4571-8e6d-4536336b1486",
                "email": "anonymous@xyz.com",
                "password": "d1e8a70b5ccab1dc2f56bbf7e99f064a660c08e361a35751b9c483c88943d082",
                "is_verified": False,
                "role": "patient",
            }
        }
