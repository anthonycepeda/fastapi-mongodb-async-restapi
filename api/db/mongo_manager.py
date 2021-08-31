import json
import os
from typing import List

from bson.json_util import dumps
from fastapi import HTTPException, status
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from api.db import DatabaseManager
from api.public.user.models import User
from api.utils.logger import logger_config

logger = logger_config(__name__)


class MongoManager(DatabaseManager):
    """
    This class extends from ./database_manager.py
    which have the abstract methods to be re-used here.
    """

    client: AsyncIOMotorClient = None
    db: AsyncIOMotorDatabase = None

    # database connect and close connections
    async def connect_to_database(self, path: str):
        logger.info("Connecting to MongoDB")
        self.client = AsyncIOMotorClient(path, maxPoolSize=10, minPoolSize=10)

        if os.getenv("ENVIRONMENT") == "PRD":
            self.db = self.client.users_prd
        elif os.getenv("ENVIRONMENT") == "STG":
            self.db = self.client.users_stg
        else:
            self.db = self.client.users_dev

        logger.info(
            "Connected to MongoDB -  %s environment!", os.getenv("ENVIRONMENT", "DEV")
        )

    async def close_database_connection(self):
        logger.info("Closing connection to MongoDB")
        self.client.close()
        logger.info("MongoDB connection closed")

    # to be used from /api/public endpoints
    async def user_get_total(self) -> int:
        total = await self.db.users.count_documents({})
        return total

    async def user_get_actives(self) -> int:
        users = self.db.users.find({"active": True})
        users_list = []
        async for user in users:
            users_list.append(json.loads(dumps(user)))

        return len(users_list)

    async def user_get_all(self) -> List[User]:
        users_list = []
        users = self.db.users.find()

        async for user in users:
            del user["_id"]
            users_list.append(json.loads(dumps(user)))

        return users_list

    async def user_get_one(self, user_id: str) -> User:
        users = self.db.users.find({"user_id": user_id})

        async for user in users:
            del user["_id"]
            return json.loads(dumps(user))

    async def user_insert_one(self, user: User) -> User:
        user_exist = await self.user_get_one(user_id=user.dict()["user_id"])
        if user_exist:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"user: {user_exist['user_id']} already exist",
            )

        await self.db.users.insert_one(user.dict())

        user = await self.user_get_one(user_id=user.dict()["user_id"])

        return user

    async def user_update_one(self, user: User) -> list:
        _user = user.dict()
        await self.db.users.update_one({"user_id": _user["user_id"]}, {"$set": _user})
        user_updated = await self.user_get_one(user_id=_user["user_id"])

        return user_updated

    async def user_delete_one(self, user: User) -> List[User]:
        await self.db.users.delete_one(user.dict())

        user_deleted = await self.user_get_one(user_id=user.dict()["user_id"])

        return user_deleted
