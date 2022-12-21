# syntax=docker/dockerfile:1

FROM python:3.8.5

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PORT=8050

WORKDIR /src

COPY . /src/

COPY requirements.txt /src/requirements.txt

RUN pip install --upgrade pip

RUN pip install -r requirements.txt


EXPOSE $PORT