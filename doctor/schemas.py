from pydantic import BaseModel


class Doctor_Schema(BaseModel):
    name: str
    degree: str
    medical_profession: str
    experience: int
    phone_number: str
    is_approved: bool
    # meta_data: Json

    class Config:
        orm_mode = True
        use_enum_values = True
        schema_extra = {
            "example": {
                "name": "John Doe",
                "degree": "MBBS",
                "medical_profession": "General Physician",
                "experience": 29,
                "phone_number": "8142111623",
                "is_approved": True,
                # "meta_data": {'blood_type': 'O+'},
            }
        }
