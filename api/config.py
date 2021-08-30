import os
import secrets
from functools import lru_cache

from pydantic import BaseSettings


def database_uri():
    """db connection"""
    DB_HOST = os.getenv("DB_HOST", "mongo")
    DB_PORT = os.getenv("DB_PORT", "27017")
    DB_NAME = os.getenv("DB_NAME", "api-db")
    DB_USERNAME = os.getenv("DB_USERNAME")
    DB_PASSWORD = os.getenv("DB_PASSWORD")

    MONGODB_CLIENT_SETUP = (
        f"mongodb://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    return MONGODB_CLIENT_SETUP


class Settings(BaseSettings):
    """app config settings"""

    PROJECT_NAME: str
    VERSION: str
    DESCRIPTION: str
    SECRET_KET: str = secrets.token_urlsafe(32)
    DEBUG: bool = bool(os.getenv("DEBUG", "False"))
    ENVIRONMENT: str
    DB_URI = database_uri()

    class Config:
        case_sensitive = True


@lru_cache
def get_config():
    return Settings()
