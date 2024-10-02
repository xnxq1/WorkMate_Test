from fastapi import APIRouter

from app.infra.db.repo.cats import ICatReader, ICatWriter
from app.domain.entities import Cat
router = APIRouter(prefix='/cats', tags=['Cats'])

@router.post('/all')
async def add_cat(cat: Cat):
    repo = ICatWriter()
    return await repo.add(cat)