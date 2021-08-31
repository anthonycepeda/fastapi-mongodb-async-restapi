![alt text](./FastAPI-MongoDB.png)

# FastAPI MongoDB Async RestAPI

### A Blueprint of a production-ready API.

> This project is based on [Michaldev](https://github.com/michaldev)'s Github [fastapi-async-mongodb](https://github.com/michaldev/fastapi-async-mongodb).</br>
> Mongo DB has been configured using [this](https://offhourscoding.com/secure-mongodb-with-docker/) articule

## Installing / Getting started

Quickstart

```shell
# build and run
$ docker-compose up --build
```

### Usage:

```shell
# build and run the project
$ docker-compose up --build

# run in background
$ docker-compose up -d

# delete docker images
$ docker-compose rm mongo api

# docker compose help
$ docker-compose --help
```

### Project Structure:

```
project
│   README.md
│   docker-compose.yaml
│   entry_point.py
│   Pipfile
│   Pipfile.lock
│
└───api/
│   │   __init__.py
│   │   config.py   # app settings
│   │   main.py     # app startup
│   │
│   └───db/
│   │   │   __init__.py
│   │   │   database_manager.py   # db abstract methods
│   │   │   mongo_manager.py      # actual mongo conn
│   │
│   └───models/
│   │   │   generic.py     # generic pydantic models
│   │
│   └───public/            # api namespaces
│   │   │   __init__.py
│   │   │
│   │   └───health/
|   │       │   models.py
|   │       │  views.py
|   │       │
│   │       users/
|   │       │   models.py
|   │       │  views.py
|   │
│   └───utlis/
│       │   __init__.py
│       │   logger.py     # custom logger
│
└───docker/           # mongo image initializer & api dockerfile
|    │   docker-entrypoint-initdb.d/mongo-init.js
|    │   Dockerfile
│
└───tavern_tests/     # api tests
    │   common.yaml
    │   test_user.tavern.yaml
```

### Help:

Installs and info:

- [Docker](https://docs.docker.com/engine/install/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Python](https://www.python.org/downloads/)

### Features:

- Framework: [Fastapi](https://github.com/tiangolo/fastapi)
- DB: [MongoDB](https://github.com/mongodb/mongo)
- Container: [docker-compose](https://github.com/docker/compose)
- dependencies:
  - [Pydantic](https://github.com/samuelcolvin/pydantic)
  - [Motor](https://github.com/mongodb/motor)
  - [uvicorn](https://github.com/encode/uvicorn)
  - [prometheus](https://github.com/prometheus/prometheus)
  - [tavern](https://github.com/taverntesting/tavern)
  - [Pytest](https://github.com/pytest-dev/pytest)
