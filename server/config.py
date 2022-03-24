from fastapi import HTTPException
from pydantic import BaseSettings, EmailStr, HttpUrl, PostgresDsn


class Settings(BaseSettings):
    TITLE: str = "HMS Auth Server"
    VERSION: str = "1.0.0"
    DESCRIPTION: str = "Auth Microservice for HMS Server"

    NAME: str = "ANONYMOUS"
    URL: HttpUrl = "https://www.anonymous.com/"
    EMAIL: EmailStr = "anonymous@xyz.com"

    LICENSE_NAME: str = "GNU GPL"

    # PGUSER: str
    # PGPASSWORD: str
    # PGHOST: str
    # PGDATABASE: str
    # PGPORT: int
    DATABASE_URL: str

    PRIVATE_KEY: str
    PUBLIC_KEY: str
    API_ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    ENVIRONMENT: str

    class Config:
        env_file = ".env"
        env_file_encoding = "UTF-8"

    # def get_connection_string(self) -> PostgresDsn:
        # return f"postgres://{self.PGUSER}:{self.PGPASSWORD}@{self.PGHOST}:{self.PGPORT}/{self.PGDATABASE}"

    def debug(self) -> bool:
        return self.ENVIRONMENT == "DEVELOPMENT"

    def invalid_credentials(self):
        return HTTPException(
            status_code=401,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )


settings = Settings()
