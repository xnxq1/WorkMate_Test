from dataclasses import dataclass

from app.infra.db.repo.base import CatReader, BreedReader
from app.domain.entities import Cat
from uuid import UUID


@dataclass
class GetAllCatsHandler:
    repo: CatReader

    async def handle(self) -> list[Cat]:
        cats = await self.repo.get_all()
        return cats


@dataclass
class GetAllCatsWithBreedHandler:
    repo: CatReader

    async def handle(self, breed_name: str) -> list[Cat]:
        cats = await self.repo.get_by_breed_name(breed_name)
        return cats


@dataclass
class GetCatByIdHandler:
    repo: CatReader

    async def handle(self, cat_id: UUID) -> Cat:
        return await self.repo.get_by_id(cat_id)

