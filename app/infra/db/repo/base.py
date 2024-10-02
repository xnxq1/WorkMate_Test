from abc import ABC, abstractmethod
from functools import wraps
from typing import Callable
from uuid import UUID
from sqlalchemy.exc import SQLAlchemyError

from app.domain.entities import Cat, Breed
from app.infra.db.repo.exceptions import BaseRepoException


def check_exception(func: Callable):
    @wraps(func)
    async def inner(*args, **kwargs):
        try:
            res = await func(*args, **kwargs)
            return res
        except SQLAlchemyError as err:
            raise BaseRepoException()

    return inner

class CatReader(ABC):


    @abstractmethod
    async def get_all(self) -> list[Cat]:
        ...

    @abstractmethod
    async def get_by_id(self, cat_id: UUID) -> Cat:
        ...

    @abstractmethod
    async def get_by_breed_name(self, breed_name: str) -> list[Cat]:
        ...

class CatWriter(ABC):

    @abstractmethod
    async def add(self, cat: Cat) -> None:
        ...
    @abstractmethod
    async def update(self, cat_id: UUID, new_data: dict) -> None:
        ...

    @abstractmethod
    async def delete(self, cat_id: UUID) -> None:
        ...


class BreedReader(ABC):

    @abstractmethod
    async def get_all(self) -> list[Breed]:
        ...

    @abstractmethod
    async def get_by_name(self, breed_name: str) -> Breed:
        ...

class BreedWriter(ABC):

    @abstractmethod
    async def add(self, breed: Breed) -> None:
        ...