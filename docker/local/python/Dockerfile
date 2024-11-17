FROM python:3

ENV PYTHONPATH=/usr/src

WORKDIR /usr/src

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .
