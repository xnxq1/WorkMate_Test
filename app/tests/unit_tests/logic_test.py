from app.logic.breeds.query import GetAllBreedsHandler
from app.tests.unit_tests.mock import CatReaderMock, BreedReaderMock
from app.logic.cats.query import GetAllCatsHandler, GetAllCatsWithBreedHandler, GetCatByIdHandler


async def test_GetAllCatsHandler():
    repo = CatReaderMock()
    handler = GetAllCatsHandler(repo)
    assert await handler.handle() == await repo.get_all()


async def test_GetAllCatsWithBreedHandler():
    repo = CatReaderMock()
    handler = GetAllCatsWithBreedHandler(repo)
    assert await handler.handle('dsgs') == await repo.get_by_breed_name('dsgs')

async def test_GetCatByIdHandler():
    repo = CatReaderMock()
    handler = GetCatByIdHandler(repo)
    assert await handler.handle('1') == await repo.get_by_id('1')


async def test_GetAllBreedsHandler():
    repo = BreedReaderMock()
    handler = GetAllBreedsHandler(repo)
    assert await handler.handle() == await repo.get_all()