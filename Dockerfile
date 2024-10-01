FROM python:3.12-slim

ENV PYTHONPATH=.

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /code

RUN pip install poetry

COPY pyproject.toml /code

RUN poetry install --without test

COPY . /code

EXPOSE 8501

ENTRYPOINT ["poetry", "run", "streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
