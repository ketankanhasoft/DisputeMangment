# Image of the language
FROM python:3.10
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
RUN python -m pip install --upgrade pip

COPY requirements.txt /app/
RUN python -m pip install -r requirements.txt

COPY . /app/