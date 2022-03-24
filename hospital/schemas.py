from pydantic import BaseModel


class Hospital_Schema(BaseModel):
    name: str
    address: str
    phone_number: str
    is_approved: bool
    # meta_data: Json

    class Config:
        orm_mode = True
        use_enum_values = True
        schema_extra = {
            "example": {
                "name": "John Doe Hospital",
                "address": "Palam Extension, Palam, New Delhi, Delhi 110077",
                "phone_number": "8142111623",
                "is_approved": True,
                # "meta_data": "{'Built on': '14-Dec-2013'}",
            }
        }
