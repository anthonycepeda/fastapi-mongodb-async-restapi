FROM python:3.10



WORKDIR /app

COPY tavern_tests /app/tavern_tests
COPY Pipfile /app
COPY Pipfile.lock /app
COPY .env /app/.env
RUN pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install --${PIPENV_ARGS}

RUN cat /etc/ssl/certs/ca-certificates.crt >> `python -m certifi`

COPY api/ /app/api
COPY entry_point.py /app/entry_point.py

ENV HOST=0.0.0.0 PORT=8080
EXPOSE ${PORT}

CMD ["pipenv", "run", "python", "entry_point.py"]