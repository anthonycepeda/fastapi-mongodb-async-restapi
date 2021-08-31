import os

from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from api.db import DatabaseManager, get_database
from api.public.health.models import Health

router = APIRouter()


@router.get(
    "",
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_200_OK: {"model": Health},
    },
)
async def health_endpoint(db: DatabaseManager = Depends(get_database)) -> Health:
    active_users = await db.user_get_actives()
    total_users = await db.user_get_total()
    health = {
        "status": "OK",
        "environment": os.getenv("ENVIRONMENT", "DEV"),
        "active_users": active_users,
        "total_users": total_users,
    }
    return JSONResponse(status_code=status.HTTP_200_OK, content=health)
