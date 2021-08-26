from typing import List, Dict, Optional

from pydantic import BaseModel, EmailStr


class Health(BaseModel):
    """Health endpoint response"""

    status: str
    environment: str
    active_users: int
    total_users: int

    class Config:
        """Swagger example"""

        schema_extra = {
            "example": {
                "status": "OK",
                "environment": "DEV",
                "active_users": 500,
                "total_users": 1200,
            }
        }


class User(BaseModel):
    """User Model"""

    user_id: str
    username: str
    name: str
    email: EmailStr
    active: bool

    class Config:
        """Swagger example"""

        schema_extra = {
            "example": {
                "user_id": "a00001",
                "username": "anth0",
                "name": "Anthony Cepeda",
                "email": "anth@mail.com",
                "active": True,
            }
        }


class Error(BaseModel):
    """Erros reponses Model"""

    detail: str
    status_code: int

    class Config:
        schema_extra = {
            "example": {
                "detail": "MongoDb not ready",
                "status_code": 406,
            }
        }
