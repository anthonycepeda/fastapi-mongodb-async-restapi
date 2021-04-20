import os
import secrets
from functools import lru_cache
from typing import Optional

from pydantic import BaseSettings, HttpUrl


def database_uri():
    MONGODB_HOST = os.getenv("MONGODB_HOST", "localhost:27017")
    MONGODB_DB_AUTH = os.getenv("MONGODB_DB_AUTH", "admin")
    MONGODB_USERNAME = os.getenv("MONGODB_USERNAME")
    MONGODB_PASSWORD = os.getenv("MONGODB_PASSWORD")

    if os.getenv("ENVIRONMENT") != "DEV":
        MONGODB_CLIENT_SETUP = f"mongodb://{MONGODB_USERNAME}:{MONGODB_PASSWORD}@{MONGODB_HOST}/{MONGODB_DB_AUTH}?tls=true"
    else:
        MONGODB_CLIENT_SETUP = f"mongodb://{MONGODB_HOST}/{MONGODB_DB_AUTH}?tls=false"
    return MONGODB_CLIENT_SETUP


class Settings(BaseSettings):
    PROJECT_NAME: str = (
        f"FastApi Mongo Async API - {os.getenv('ENVIRONMENT', 'DEV').capitalize()}"
    )
    VERSION: str = "v1.0.0"
    DESCRIPTION: str = (
        "A Production Ready FastAPI API using Asyncronous MongoDB Connection"
    )
    SECRET_KET: str = secrets.token_urlsafe(32)
    SENTRY_DSN: Optional[HttpUrl] = os.getenv("SENTRY_DSN")
    DEBUG: bool = bool(os.getenv("DEBUG", "False"))
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "DEV").capitalize()
    DB_URI = database_uri()

    class Config:
        case_sensitive = True


@lru_cache
def get_config():
    return Settings()
