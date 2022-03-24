from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from server.config import settings
from users.auth import router as Auth_Router
from patient.router import router as Patient_Router
from doctor.router import router as Doctor_Router
from hospital.router import router as Hospital_Router
from staff.router import router as Staff_Router

tags_metadata = [
    {"name": "Users", "description": "HMS Auth Server"},
    {"name": "Doctors", "description": "HMS Doctors"},
    {"name": "Patients", "description": "HMS Patients"},
    {"name": "Hospitals", "description": "HMS Hospitals"},
    {"name": "Staff", "description": "HMS Staff"},
]

app = FastAPI(
    title=settings.TITLE,
    version=settings.VERSION,
    description=settings.DESCRIPTION,
    contact={
        "name": settings.NAME,
        "url": settings.URL,
        "email": settings.EMAIL,
    },
    license_info={
        "name": settings.LICENSE_NAME,
        # "url": settings.LICENSE_URL,
    },
    openapi_tags=tags_metadata,
)

ALLOWED_HOSTS = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_HOSTS,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.include_router(Auth_Router)
app.include_router(Patient_Router)
app.include_router(Doctor_Router)
app.include_router(Hospital_Router)
app.include_router(Staff_Router)


@app.get("/health", status_code=200)
def health_check():
    return "Server is healthy"
