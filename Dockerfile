FROM python:3.12.8-slim

ENV PYTHONPATH=.

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /code

RUN pip install uv

RUN uv python pin 3.12.8

COPY pyproject.toml /code

RUN uv sync --no-group test

COPY main.py /code/main.py

COPY resources /code/resources

COPY src /code/src

COPY .streamlit /code/.streamlit

EXPOSE 8501

CMD ["uv", "run", "streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
