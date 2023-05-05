FROM python:3.9-slim-bullseye AS base

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      git make build-essential libpq-dev vim less && \
    rm -rf /var/lib/apt/lists/*


FROM base as sa1_3

RUN pip3 install sqlalchemy==1.3.23

WORKDIR /app
COPY . .
RUN pip3 install -e '.[test]'


FROM base as sa1_4

RUN pip3 install sqlalchemy>1.4.0

WORKDIR /app
COPY . .
RUN pip3 install -e '.[test]'

