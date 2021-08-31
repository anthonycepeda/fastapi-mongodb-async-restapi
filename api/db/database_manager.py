from abc import abstractmethod
from typing import List

from api.public.user.models import User


class DatabaseManager:
    """
    This class is meant to be extended from
    ./mongo_manager.py which will be the actual connection to mongodb.
    """

    @property
    def client(self):
        raise NotImplementedError

    @property
    def db(self):
        raise NotImplementedError

    # database connect and close connections
    @abstractmethod
    async def connect_to_database(self, path: str):
        pass

    @abstractmethod
    async def close_database_connection(self):
        pass

    # to be used from /api/public endpoints
    @abstractmethod
    async def user_get_total(self) -> int:
        pass

    @abstractmethod
    async def user_get_actives(self) -> int:
        pass

    @abstractmethod
    async def user_get_all(self) -> List[User]:
        pass

    @abstractmethod
    async def user_get_one(self, user_id: str) -> List[User]:
        pass

    @abstractmethod
    async def user_insert_one(self, user: User) -> List[User]:
        pass

    @abstractmethod
    async def user_update_one(self, user: User) -> List[User]:
        pass

    @abstractmethod
    async def user_delete_one(self, user: User) -> List[User]:
        pass
