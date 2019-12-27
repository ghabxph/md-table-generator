FROM python:3.9.0a2-alpine3.10

COPY . /app
ENTRYPOINT ["python", "/app/script.py"]