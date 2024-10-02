from app.infra.db.repo.breeds import IBreedReader
from app.infra.db.repo.cats import ICatReader, ICatWriter
from app.logic.cats.command import AddCatHandler, UpdateCatHandler, DeleteCatHandler
from app.logic.cats.query import GetAllCatsHandler, GetAllCatsWithBreedHandler, GetCatByIdHandler


def GetAllCatsHandler_factory() -> GetAllCatsHandler:
    repo = ICatReader()
    return GetAllCatsHandler(repo=repo)

def GetAllCatsWithBreedHandler_factory() -> GetAllCatsWithBreedHandler:
    repo = ICatReader()
    return GetAllCatsWithBreedHandler(repo=repo)


def GetCatByIdHandler_factory() -> GetCatByIdHandler:
    repo = ICatReader()
    return GetCatByIdHandler(repo=repo)

def AddCatHandler_factory() -> AddCatHandler:
    cat_repo = ICatWriter()
    breed_repo = IBreedReader()
    return AddCatHandler(cat_repo=cat_repo, breed_repo=breed_repo)


def UpdateCatHandler_factory() -> UpdateCatHandler:
    cat_repo = ICatWriter()
    breed_repo = IBreedReader()
    return UpdateCatHandler(cat_repo=cat_repo, breed_repo=breed_repo)


def DeleteCatHandler_factory() -> DeleteCatHandler:
    repo = ICatWriter()
    return DeleteCatHandler(repo=repo)