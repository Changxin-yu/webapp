FROM python:3
RUN apt-get update
RUN pip install flask
COPY app.py /app.py

ENTRYPOINT FLASH_APP=/opt/app.py flask run --host=0.0.0.0
