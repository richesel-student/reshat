FROM python:3.11-slim AS builder

WORKDIR /app



# Устанавливаем системные зависимости для сборки uwsgi
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libpq-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*


COPY pyproject.toml pdm.lock /app/

#COPY requirements.txt ./

RUN pip install pdm

RUN pdm venv create --force \
    && PDM_VENV=/app/.venv pdm install --prod --no-lock --no-editable


RUN pip install pdm
#COPY . /app/merch_project
RUN pdm venv create --force \
    && PDM_VENV=/app/.venv pdm install --prod --no-lock --no-editable

#COPY . /app/app_payment
COPY . /app/

RUN apt-get update && apt-get install -y netcat-openbsd && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y libpq5 && rm -rf /var/lib/apt/lists/*
##COPY . /app/


#WORKDIR /app/app_payment
WORKDIR /app/payment
COPY docker-entrypoint.sh /docker-entrypoint.sh


RUN chmod 777 /docker-entrypoint.sh

ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 8000

ENTRYPOINT ["/docker-entrypoint.sh"]
