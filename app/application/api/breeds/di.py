from app.infra.db.repo.breeds import IBreedReader, IBreedWriter
from app.logic.breeds.command import AddBreedHandler
from app.logic.breeds.query import GetAllBreedsHandler


def GetAllBreedsHandler_factory() -> GetAllBreedsHandler:
    repo = IBreedReader()
    return GetAllBreedsHandler(repo=repo)

def AddBreedHandler_factory() -> AddBreedHandler:
    repo = IBreedWriter()
    return AddBreedHandler(repo=repo)