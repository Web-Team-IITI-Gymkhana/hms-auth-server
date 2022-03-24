from pydantic import BaseModel, UUID4


class Staff_Terminate(BaseModel):
    doctor_uuid: UUID4

    class Config:
        orm_mode = True
        use_enum_values = True
        schema_extra = {
            "example": {
                "doctor_uuid": "43cac6dd-ce7c-4b60-8652-3bc76a5d8c85",
            }
        }


class Staff_Create(Staff_Terminate):
    position: str

    class Config:
        orm_mode = True
        use_enum_values = True
        schema_extra = {
            "example": {
                "doctor_uuid": "43cac6dd-ce7c-4b60-8652-3bc76a5d8c85",
                "position": "Head of Surgery",
            }
        }
