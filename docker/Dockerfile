# Dockerfile Doc: https://docs.docker.com/engine/reference/builder/
# using python 3.9 docker image
FROM python:3.9

# letting docker know the port
EXPOSE 8080

# picking vars from system enviroments
# you should: export variable_name=value in deployment OS
ARG environment
ARG sentry_dsn
ARG mongo_host
ARG mongo_db_auth
ARG mongo_username
ARG mongo_password

# loading vars to be used from os.getenv()
ENV MONGODB_HOST=${mongo_host}
ENV MONGODB_DB_AUTH=${mongo_db_auth}
ENV MONGODB_USERNAME=${mongo_username}
ENV MONGODB_PASSWORD=${mongo_password}
ENV ENVIRONMENT=${entry_point}
ENV SENTRY_DSN=${sentry_dsn}

# setting working directory
WORKDIR /app

# installing pip's requirements file
COPY requirements/ /app/requirements
RUN pip install --upgrade pip
RUN pip install -r ./requirements/base.txt --no-cache-dir

# copying the api and it's access point
COPY api/ /app/api
COPY entry_point.py /app/entry_point.py

# runing the app
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8080", "--access-log", "--reload"]