FROM python:3.11.4-slim-buster

WORKDIR /workdir

COPY ./requirements.txt /workdir/requirements.txt

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt


COPY ./app/ workdir/app/

ENV PYTHONPATH=/app

