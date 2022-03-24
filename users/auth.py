from uuid import uuid4

from fastapi import APIRouter, Depends, Header, HTTPException
from server.config import settings
from server.dependencies import get_db
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from .models import User
from .processes import (
    add_blacklist_token,
    authenticate_user,
    get_password_hash,
    get_token,
)
from .schemas import UserId, UserCredentials

router = APIRouter(prefix="/auth", tags=["Users"])


@router.post("/register", status_code=200)
async def register(user: UserId, db: Session = Depends(get_db)):
    record = db.query(User).filter(User.email == user.email).first()
    if record is not None:
        return HTTPException(
            status_code=401,
            detail="User Already Exists",
            headers={"WWW-Authenticate": "Bearer"},
        )
    entry = User(
        uuid=uuid4(),
        email=user.email,
        role=user.role,
        password=get_password_hash(user.password),
        is_verified=False,
    )
    db.add(entry)
    db.commit()
    db.refresh(entry)
    return "User Registered successfully"


@router.post("/login")
async def login(user_id: UserCredentials, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == user_id.email).first()
    if not user:
        return HTTPException(
            status_code=401,
            detail="Invalid Email",
            headers={"WWW-Authenticate": "Bearer"},
        )
    user = authenticate_user(user.uuid, user_id.password, db)
    if not user:
        raise settings.invalid_credentials()

    access_token = get_token(uuid=user.uuid)

    return {
        "access_token": access_token,
        "is_verified": user.is_verified,
        "token_type": "bearer",
    }


@router.get("/logout")
def logout(token: str = Header(None)):
    if add_blacklist_token(token):
        return JSONResponse({"result": True})
    raise settings.invalid_credentials()
