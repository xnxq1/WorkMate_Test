from dataclasses import dataclass

from pydantic import BaseModel, Field
from uuid import UUID
from app.domain.entities import Color, Cat
from app.infra.db.repo.base import CatWriter, BreedReader


class AddCatCommand(BaseModel):
    name: str = Field(min_length=0, max_length=255)
    color: Color
    age_in_month: int = Field(gt=0)
    breed_name: str


@dataclass
class AddCatHandler:
    cat_repo: CatWriter
    breed_repo: BreedReader

    async def handle(self, command: AddCatCommand) -> None:
        breed = await self.breed_repo.get_by_name(command.breed_name)
        breed_id = breed.id
        cat = Cat(name=command.name, color=command.color, age_in_month=command.age_in_month, breed_id=breed_id)
        await self.cat_repo.add(cat)


class UpdateCatCommand(BaseModel):
    name: str | None= Field(min_length=0, max_length=255, default=None)
    color: Color | None = Field(default=None)
    age_in_month: int | None= Field(gt=0, default=None)
    breed_name: str | None = Field(default=None)



@dataclass
class UpdateCatHandler:
    cat_repo: CatWriter
    breed_repo: BreedReader

    async def handle(self, cat_id: UUID, command: UpdateCatCommand) -> None:
        filter_command = {key: value for key, value in dict(command).items() if
                          value is not None and key != 'breed_name'}
        if command.breed_name is not None:
            breed = await self.breed_repo.get_by_name(command.breed_name)
            breed_id = breed.id
            filter_command['breed_id'] = breed_id

        await self.cat_repo.update(cat_id, filter_command)

@dataclass
class DeleteCatHandler:
    repo: CatWriter


    async def handle(self, cat_id: UUID) -> None:
        await self.repo.delete(cat_id)

