from fastapi import APIRouter, Depends, Header
from patient.schemas import Patient_Schema
from server.dependencies import get_db
from sqlalchemy.orm import Session

from .models import Patient
from users.processes import (
    get_current_user,
)

router = APIRouter(prefix="/patient", tags=["Patients"])


@router.get("/details")
async def user_details(token: str = Header(None), db: Session = Depends(get_db)):
    user = await get_current_user(token, db)
    data = db.query(Patient).filter(Patient.uuid == user.uuid).first()
    return data


@router.post("/meta_data")
async def user_details(
    body: Patient_Schema, token: str = Header(None), db: Session = Depends(get_db)
):
    user = await get_current_user(token, db)

    entry = Patient(**body.dict(), uuid=user.uuid, details_filled=True)
    db.add(entry)
    db.commit()
    return "Successfully added"
