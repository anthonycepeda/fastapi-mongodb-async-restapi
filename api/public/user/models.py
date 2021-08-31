from pydantic import BaseModel, EmailStr


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
