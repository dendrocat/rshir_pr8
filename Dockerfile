FROM python:3.11.5


RUN apt-get update \
    && apt-get install -y libmariadb-dev \
    && apt-get install -y python3-pip \
    && apt-get install -y build-essential \
    && apt-get install -y libcurl4-openssl-dev \
    && apt-get install -y libssl-dev \
    && pip install --upgrade pip

RUN pip install --upgrade pip

RUN mkdir -p /app
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt
