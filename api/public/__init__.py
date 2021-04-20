from fastapi import APIRouter

from api.public.health import views as health
from api.public.user import views as user

api = APIRouter()

api.include_router(health.router, prefix="/health", tags=["Health"])
api.include_router(user.router, prefix="/user", tags=["Users"])
