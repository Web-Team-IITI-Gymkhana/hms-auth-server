from pydantic import BaseModel


class Patient_Schema(BaseModel):
    nhid: int
    name: str
    gender: str
    age: int
    address: str
    # meta_data: Json

    class Config:
        orm_mode = True
        use_enum_values = True
        schema_extra = {
            "example": {
                "nhid": "2000010",
                "name": "John Doe",
                "gender": "male",
                "age": 24,
                "address": "Agra, Uttar Pradesh",
                # "meta_data": "{'blood_type': 'O+'}",
            }
        }
