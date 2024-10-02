from app.domain.entities import Breed as Breed_entity
from app.infra.db.conn import db
from app.infra.db.models import Breed as Breed_db
from app.infra.db.repo.base import BreedReader, BreedWriter, check_exception
from sqlalchemy import select, insert


class IBreedReader(BreedReader):

    async def get_all(self) -> list[Breed_entity]:
        async with db.session_factory() as session:
            query = select(Breed_db)
            result = await session.execute(query)

            return result.scalars().all()


class IBreedWriter(BreedWriter):

    @check_exception
    async def add(self, breed: Breed_entity) -> None:
        async with db.session_factory() as session:
            stmt = insert(Breed_db).values(**breed)
            await session.execute(stmt)
            await session.commit()