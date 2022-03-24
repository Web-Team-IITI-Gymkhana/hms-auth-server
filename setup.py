from setuptools import setup, find_packages
from server.config import settings

setup(
    name="hms_auth_server",
    version=settings.VERSION,
    description=settings.DESCRIPTION,
    author=settings.NAME,
    author_email=settings.EMAIL,
    url=settings.URL,
    license=settings.LICENSE_NAME,
    packages=find_packages(),
)
