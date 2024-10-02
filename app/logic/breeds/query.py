from dataclasses import dataclass

from app.domain.entities import Breed
from app.infra.db.repo.base import BreedReader


@dataclass
class GetAllBreedsHandler:
    repo: BreedReader

    async def handle(self) -> list[Breed]:
        breeds = await self.repo.get_all()
        return breeds