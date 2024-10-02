from sqlalchemy import select, insert, update, delete

from app.infra.db.conn import db
from app.infra.db.repo.exceptions import NotCatException, NotCatsWithThisBreedException
from app.infra.db.repo.base import CatReader, CatWriter, check_exception
from app.infra.db.models import Cat as Cat_db, Breed
from app.domain.entities import Cat as Cat_entity


class ICatReader(CatReader):


    async def get_all(self) -> list[Cat_entity]:
        async with db.session_factory() as session:
            query = select(Cat_db)
            result = await session.execute(query)
            result = result.scalars().all()

            return result

    async def get_by_id(self, cat_id: int) -> Cat_entity:
        async with db.session_factory() as session:
            query = select(Cat_db).where(Cat_db.id == cat_id)
            result = await session.execute(query)
            result = result.scalar_one_or_none()

            if not result:
                raise NotCatException(cat_id)

            return result

    async def get_by_breed_name(self, breed_name: str) -> list[Cat_entity]:
        async with db.session_factory() as session:
            query = select(Cat_db).join(Breed).where(Breed.name == breed_name)
            result = await session.execute(query)

            if not result:
                raise NotCatsWithThisBreedException(breed_name)

            return result

class ICatWriter(CatWriter):

    @check_exception
    async def add(self, cat: Cat_entity) -> None:
        async with db.session_factory() as session:
            stmt = insert(Cat_db).values(**cat)
            await session.execute(stmt)
            await session.commit()

    @check_exception
    async def update(self, cat: Cat_entity) -> None:
        async with db.session_factory() as session:
            stmt = update(Cat_db).values(**cat).where(Cat_db.id == cat['id'])
            await session.execute(stmt)
            await session.commit()


    @check_exception
    async def delete(self, cat_id: int) -> None:
        async with db.session_factory() as session:
            stmt = delete(Cat_db).where(Cat_db.id == cat_id)
            await session.execute(stmt)
            await session.commit()
