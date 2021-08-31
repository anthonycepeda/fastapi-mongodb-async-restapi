from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse

from api.db import DatabaseManager, get_database
from api.models.generic import Error
from api.public.user.models import User
from api.utils.logger import logger_config

logger = logger_config(__name__)

router = APIRouter()


@router.get(
    "",
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_200_OK: {"model": List[User]},
        status.HTTP_406_NOT_ACCEPTABLE: {"model": Error},
    },
)
async def get_all_users_in_database(
    db: DatabaseManager = Depends(get_database),
) -> List[User]:
    """Get all users from users mongodb collection"""
    users = await db.user_get_all()
    if users:
        return JSONResponse(status_code=status.HTTP_200_OK, content=users)
    raise HTTPException(
        status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="database not ready"
    )


@router.get(
    "/{user_id}",
    responses={
        status.HTTP_200_OK: {"model": User},
        status.HTTP_404_NOT_FOUND: {"model": Error},
    },
)
async def get_user_by_user_id(
    user_id: str, db: DatabaseManager = Depends(get_database)
) -> User:
    """Get one user by providing a user_id: str"""
    user = await db.user_get_one(user_id=user_id)

    if user:
        return JSONResponse(status_code=status.HTTP_200_OK, content=user)

    raise HTTPException(
        status_code=status.HTTP_406_NOT_ACCEPTABLE,
        detail=f"no user found with user_id: {user_id}",
    )


@router.put(
    "",
    responses={
        status.HTTP_201_CREATED: {"model": User},
        status.HTTP_409_CONFLICT: {"model": Error},
    },
)
async def insert_a_new_user(
    payload: User, db: DatabaseManager = Depends(get_database)
) -> User:
    user_created = await db.user_insert_one(user=payload)

    if user_created:
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=user_created)

    raise HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail=f"user could not be created",
    )


@router.patch(
    "",
    responses={
        status.HTTP_202_ACCEPTED: {"model": User},
        status.HTTP_409_CONFLICT: {"model": Error},
    },
)
async def update_a_user(
    payload: User, db: DatabaseManager = Depends(get_database)
) -> User:
    user_updated = await db.user_update_one(user=payload)

    if user_updated:
        return JSONResponse(status_code=status.HTTP_202_ACCEPTED, content=user_updated)

    raise HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail="user could not be updated",
    )


@router.delete(
    "",
    responses={
        status.HTTP_202_ACCEPTED: {"model": User},
        status.HTTP_409_CONFLICT: {"model": Error},
    },
)
async def delete_a_user(
    payload: User, db: DatabaseManager = Depends(get_database)
) -> list:
    user_deleted = await db.user_delete_one(user=payload)

    if not user_deleted:
        return JSONResponse(status_code=status.HTTP_202_ACCEPTED, content=[])

    raise HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail=f"user could not be deleted",
    )
