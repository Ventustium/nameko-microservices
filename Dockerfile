FROM python:3.10.5-slim

WORKDIR /data/application

COPY requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

COPY . .