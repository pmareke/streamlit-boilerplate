FROM python:3.12-slim

ENV PYTHONPATH=.

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /code

RUN pip install uv

COPY pyproject.toml /code

RUN uv sync

COPY . /code

EXPOSE 8501

ENTRYPOINT ["uv", "run", "streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
