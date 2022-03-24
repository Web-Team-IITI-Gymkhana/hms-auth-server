from staff.models import Staff
from datetime import date
from fastapi import APIRouter, Depends, Header
from server.config import settings
from staff.schemas import Staff_Create, Staff_Terminate
from server.dependencies import get_db
from sqlalchemy.orm import Session
from sqlalchemy import desc

from users.processes import (
    get_current_user,
)

router = APIRouter(prefix="/staff", tags=["Staff"])


@router.post("/add_staff")
async def add_staff(
    staff: Staff_Create, token: str = Header(None), db: Session = Depends(get_db)
):
    user = await get_current_user(token, db)
    if user.role == "hospital":
        entry = Staff(
            hospital_uuid=user.uuid,
            doctor_uuid=staff.doctor_uuid,
            position=staff.position,
        )
        db.add(entry)
        db.commit()
        return "Staff successfully Added"
    return settings.invalid_credentials


@router.post("/terminate_staff")
async def terminate_staff(
    staff: Staff_Terminate, token: str = Header(None), db: Session = Depends(get_db)
):
    user = await get_current_user(token, db)
    if user.role == "hospital":
        record = (
            db.query(Staff)
            .filter(
                Staff.hospital_uuid == user.uuid, Staff.doctor_uuid == staff.doctor_uuid
            )
            .order_by(desc(Staff.start_date))
            .first()
        )
        record.end_date = date.today()
        db.commit()
        return "Staff successfully Terminated"
    return settings.invalid_credentials


@router.get("/records")
async def records(token: str = Header(None), db: Session = Depends(get_db)):
    user = await get_current_user(token, db)
    if user.role == "hospital":
        record = (
            db.query(Staff)
            .filter(Staff.hospital_uuid == user.uuid)
            .order_by(Staff.start_date)
            .all()
        )
        return record
    elif user.role == "doctor":
        record = (
            db.query(Staff)
            .filter(Staff.doctor_uuid == user.uuid)
            .order_by(desc(Staff.start_date))
            .all()
        )
        return record
    return settings.invalid_credentials()
