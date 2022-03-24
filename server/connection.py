from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from server.config import settings

debug = settings.debug()
connection_string = settings.DATABASE_URL

engine = create_engine(connection_string, echo=debug)

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)
