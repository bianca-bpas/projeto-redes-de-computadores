FROM python:slim

WORKDIR /app

COPY src/ /app/src/

ENV PYTHONUNBUFFERED=1



