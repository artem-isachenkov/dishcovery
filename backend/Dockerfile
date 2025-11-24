FROM python:3.13

WORKDIR /src

COPY pyproject.toml poetry.lock ./
RUN pip install poetry && poetry install --no-root

COPY ./src /src

CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
