from dataclasses import dataclass

from pydantic import BaseModel, Field

from app.domain.entities import Breed
from app.infra.db.repo.base import BreedWriter

class AddBreedCommand(BaseModel):
    name: str = Field(min_length=0, max_length=255)

@dataclass
class AddBreedHandler:
    repo: BreedWriter

    async def handle(self, command: AddBreedCommand) -> None:
        breed = Breed(name=command.name)
        return await self.repo.add(breed)
