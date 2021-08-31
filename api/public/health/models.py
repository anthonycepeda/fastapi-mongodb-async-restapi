from pydantic import BaseModel


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
