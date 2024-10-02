from uuid import UUID, uuid4

from app.domain.entities import Cat, Color, Breed
from app.infra.db.repo.base import CatReader, BreedReader


class CatReaderMock(CatReader):

    async def get_all(self) -> list[Cat]:

        cats = [
            Cat(id='b5a32451-5275-4c28-9e3e-851b5e4bd59d', name='тайлер', color=Color.ginger, age_in_month=4, breed_id='6f9bed9d-9c1a-4031-808f-3a8ff31157c1'),
            Cat(id='07c1b1a4-b510-4464-9a1d-23d08444243d', name='mock', color=Color.black, age_in_month=9, breed_id='6f9bed9d-9c1a-4031-808f-3a8ff31157c1')]

        return cats

    async def get_by_id(self, cat_id: UUID) -> Cat:
        cat = Cat(id='b5a32451-5275-4c28-9e3e-851b5e4bd59d', name='тайлер', color=Color.ginger, age_in_month=4,
                breed_id='6f9bed9d-9c1a-4031-808f-3a8ff31157c1')
        return cat

    async def get_by_breed_name(self, breed_name: str) -> list[Cat]:
        cats = [
            Cat(id='b5a32451-5275-4c28-9e3e-851b5e4bd59d', name='тайлер', color=Color.ginger, age_in_month=4,
                breed_id='6f9bed9d-9c1a-4031-808f-3a8ff31157c1'),
            Cat(id='07c1b1a4-b510-4464-9a1d-23d08444243d', name='mock', color=Color.black, age_in_month=9,
                breed_id='6f9bed9d-9c1a-4031-808f-3a8ff31157c1')]

        return cats


class BreedReaderMock(BreedReader):

    async def get_all(self) -> list[Breed]:
        breeds = [
            Breed(id='b5a32451-5275-4c28-9e3e-851b5e4bd59d', name='тайлер'),
            Breed(id='07c1b1a4-b510-4464-9a1d-23d08444243d', name='mock')]
        return breeds

    async def get_by_name(self, breed_name: str) -> Breed:
        ...