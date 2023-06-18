FROM python:3.11

ENV FLASK_APP=src/main.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=development
ENV PYTHONPATH=./src

ENV POETRY_VERSION=1.5
RUN pip install "poetry==$POETRY_VERSION" && poetry config virtualenvs.create false


WORKDIR /code
COPY ./pyproject.toml ./poetry.lock* /code/

RUN poetry install --with test --no-interaction --no-ansi 

COPY . /code/

CMD ["flask", "run"]