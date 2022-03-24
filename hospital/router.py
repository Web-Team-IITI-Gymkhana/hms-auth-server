from fastapi import APIRouter, Depends, Header
from hospital.schemas import Hospital_Schema
from server.dependencies import get_db
from sqlalchemy.orm import Session
from uuid import UUID

from .models import Hospital
from users.processes import (
    get_current_user,
)

router = APIRouter(prefix="/hospital", tags=["Hospitals"])


@router.get("/")
def get_all_hospitals(db: Session = Depends(get_db)):
    data = db.query(Hospital).all()
    return data


@router.get("/{uuid}")
def retrieve_hospital(uuid: str, db: Session = Depends(get_db)):
    data = db.query(Hospital).filter(Hospital.uuid == UUID(uuid)).first()
    return data


@router.get("/details")
async def user_details(token: str = Header(None), db: Session = Depends(get_db)):
    user = await get_current_user(token, db)
    data = db.query(Hospital).filter(Hospital.uuid == user.uuid).first()
    return data


@router.post("/meta_data")
async def user_details(
    body: Hospital_Schema, token: str = Header(None), db: Session = Depends(get_db)
):
    user = await get_current_user(token, db)

    entry = Hospital(**body.dict(), uuid=user.uuid, details_filled=True)
    db.add(entry)
    db.commit()
    return "Successfully added"
