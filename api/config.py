import os
import secrets
from functools import lru_cache

from pydantic import BaseSettings


def database_uri():
    """db connection"""
    MONGO_HOST = os.getenv("MONGO_HOST", "localhost")
    MONGO_PORT = os.getenv("MONGO_PORT", "27017")
    MONGO_INITDB_ROOT_USERNAME = os.getenv("MONGO_INITDB_ROOT_USERNAME", "admin")
    MONGO_USERNAME = os.getenv("MONGO_USERNAME")
    MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")

    MONGODB_CLIENT_SETUP = f"mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_INITDB_ROOT_USERNAME}"

    return MONGODB_CLIENT_SETUP


class Settings(BaseSettings):
    """app config settings"""

    PROJECT_NAME: str
    VERSION: str = "v1.0.0"
    DESCRIPTION: str = (
        "A Production Ready FastAPI API using Asyncronous MongoDB Connection"
    )
    SECRET_KET: str = secrets.token_urlsafe(32)
    DEBUG: bool = bool(os.getenv("DEBUG", "False"))
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "DEV").capitalize()
    DB_URI = database_uri()

    class Config:
        case_sensitive = True


@lru_cache
def get_config():
    return Settings()
