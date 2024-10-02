from fastapi import APIRouter, Depends

from app.application.api.cats.di import GetAllCatsHandler_factory, GetAllCatsWithBreedHandler_factory, \
    AddCatHandler_factory, GetCatByIdHandler_factory, UpdateCatHandler_factory, DeleteCatHandler_factory
from app.domain.entities import Cat
from uuid import UUID

from app.logic.cats.command import AddCatCommand, AddCatHandler, UpdateCatHandler, UpdateCatCommand, DeleteCatHandler
from app.logic.cats.query import GetAllCatsHandler, GetAllCatsWithBreedHandler, GetCatByIdHandler

router = APIRouter(prefix='/cats', tags=['Cats'])

@router.get('/all')
async def get_all_cats_endpoint(
        handler: GetAllCatsHandler = Depends(GetAllCatsHandler_factory)) -> list[Cat]:

    return await handler.handle()

@router.get('/all/{breed_name}')
async def get_all_cats_with_breed_endpoint(
        breed_name: str,
        handler: GetAllCatsWithBreedHandler = Depends(GetAllCatsWithBreedHandler_factory)) -> list[Cat]:

    return await handler.handle(breed_name)

@router.get('/{cat_id}')
async def get_cat_by_id_endpoint(
        cat_id: UUID,
        handler: GetCatByIdHandler = Depends(GetCatByIdHandler_factory)) -> Cat:
    return await handler.handle(cat_id)

@router.post('/add')
async def add_cat_endpoint(
        cat: AddCatCommand,
        handler: AddCatHandler = Depends(AddCatHandler_factory)) -> None:

    return await handler.handle(cat)


@router.patch('/update')
async def update_cat_endpoint(
        cat_id: UUID,
        cat: UpdateCatCommand,
        handler: UpdateCatHandler = Depends(UpdateCatHandler_factory)) -> None:
    return await handler.handle(cat_id, cat)


@router.delete('/delete/{cat_id}')
async def delete_cat_endpoint(
        cat_id: UUID,
        handler: DeleteCatHandler = Depends(DeleteCatHandler_factory)) -> None:
    return await handler.handle(cat_id)

