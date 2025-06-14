FROM python:3.12.8-slim

ENV PATH="/code/.venv/bin:$PATH"

ENV PYTHONPATH=.

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /code

RUN uv python pin 3.12.8

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --locked --no-install-project --no-group dev

COPY pyproject.toml /code

COPY uv.lock /code/uv.lock

COPY main.py /code/main.py

COPY resources /code/resources

COPY .streamlit /code/.streamlit

COPY src /code/src

RUN --mount=type=cache,target=/root/.cache/uv uv sync --locked --no-group dev

EXPOSE 8501

CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
