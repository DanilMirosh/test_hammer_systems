FROM python:3.8.1-alpine

ENV PYTHONUNBUFFERED 1


WORKDIR /backend

RUN apk update && apk add python3-dev \
                        gcc \
                        libc-dev \
                        bash \
                        postgresql-dev


RUN apk add tzdata

RUN pip install --upgrade pip
RUN pip install --upgrade pip setuptools wheel


COPY ./requirements.txt /backend/requirements.txt
RUN pip install -r requirements.txt

COPY . /backend

EXPOSE 1337