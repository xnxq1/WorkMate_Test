from fastapi import APIRouter
from fastapi.params import Depends

from app.application.api.breeds.di import GetAllBreedsHandler_factory, AddBreedHandler_factory
from app.domain.entities import Breed
from app.logic.breeds.command import AddBreedCommand, AddBreedHandler
from app.logic.breeds.query import GetAllBreedsHandler

router = APIRouter(prefix='/breeds', tags=['Breeds'])

@router.get('/all')
async def get_all_breeds_endpoint(
        handler: GetAllBreedsHandler = Depends(GetAllBreedsHandler_factory)) -> list[Breed]:

    return await handler.handle()

@router.post('/add')
async def add_breed_endpoint(
        breed: AddBreedCommand,
        handler: AddBreedHandler = Depends(AddBreedHandler_factory)) -> None:

    return await handler.handle(breed)

