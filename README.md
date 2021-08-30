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

## Project Structure:
- api:
```shell
db/

```




## Features:

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

## Help:

Installs and info:

- [Docker](https://docs.docker.com/engine/install/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Python](https://www.python.org/downloads/)
