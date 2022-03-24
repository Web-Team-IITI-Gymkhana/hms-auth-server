from time import time
from pydantic import UUID4
from server.config import settings

from fastapi import Depends, FastAPI, HTTPException
from jose import jwt
from passlib.context import CryptContext
from server.dependencies import get_db
from sqlalchemy.orm import Session

from .schemas import Token, TokenData, User_Schema
from .models import User, Blacklisted_Token


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


app = FastAPI()


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def get_user(uuid: UUID4, db: Session):
    user = db.query(User).filter(User.uuid == uuid).first()
    if user is not None:
        return User_Schema(**user.__dict__)


def get_token(uuid: UUID4, role: str):
    token_expires_in = settings.ACCESS_TOKEN_EXPIRE_MINUTES
    token = create_token(
        data={"sub": str(uuid), "typ": "access"},
        expires_in=token_expires_in,
    )
    return token


def authenticate_user(uuid: UUID4, password: str, db: Session):
    user = get_user(uuid, db)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


def create_token(data: dict, expires_in: int):
    issued_at = int(time())
    expires_on = issued_at + (expires_in * 60)
    json_web_token = {"iss": settings.URL, "exp": expires_on, "iat": issued_at}
    json_web_token.update(data)
    encoded_jwt = jwt.encode(
        json_web_token, settings.PRIVATE_KEY, algorithm=settings.API_ALGORITHM
    )
    return encoded_jwt


def decode_token(token):
    return jwt.decode(
        token,
        settings.PRIVATE_KEY,
        algorithms=[settings.API_ALGORITHM],
        options={"require": ["exp", "iss", "sub", "iat"]},
    )


async def get_current_user(token: str, db: Session):
    if is_token_blacklisted({"token": token}, db):
        raise settings.invalid_credentials()
    try:
        payload = decode_token(token)
        uuid: UUID4 = UUID4(payload.get("sub"))
        if uuid is None:
            raise settings.invalid_credentials()
        token_data = TokenData(uuid=uuid)
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=401,
            detail="Token Expired",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except jwt.PyJWTError:
        raise settings.invalid_credentials()
    user = get_user(token_data.uuid, db)
    if user is None:
        raise settings.invalid_credentials()
    return user


# async def refresh_token(token):
#     try:
#         payload = decode_token(token)
#         email: str = payload.get("sub")
#         user_type: str = payload.get("user_type")

#         if email is None:
#             raise settings.invalid_credentials()
#         return JSONResponse(
#             {"result": True, "access_token": get_token(email, user_type, "access")}
#         )
#     except jwt.ExpiredSignatureError:
#         raise HTTPException(
#             status_code=401,
#             detail="Token Expired",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     except jwt.PyJWTError:
#         raise settings.invalid_credentials()


def is_token_blacklisted(token: Token, db: Session) -> bool:
    blacklist_token = (
        db.query(Blacklisted_Token)
        .filter(Blacklisted_Token.token == token["token"])
        .first()
    )
    if blacklist_token is None:
        return False
    return True


def add_blacklist_token(token: str, db: Session = Depends(get_db)) -> bool:
    try:
        blacklist_token = Blacklisted_Token(token=token)
        db.add(blacklist_token)
        db.commit()
        return True
    except:
        return False
