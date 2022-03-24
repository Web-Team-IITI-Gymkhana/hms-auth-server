FROM python:3.9
COPY . ./app
COPY ./requirements.txt ./app/requirements.txt
WORKDIR app

EXPOSE 8000:8000
RUN pip install -r requirements.txt
RUN alembic upgrade heads
CMD [ "uvicorn", "main:app" ]