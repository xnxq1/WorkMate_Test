from fastapi import FastAPI
from app.application.api.cats.router import router as cat_router
from app.application.api.breeds.router import router as breed_router


def create_app() -> FastAPI:
    app = FastAPI(
        title='Test'
    )
    app.include_router(cat_router)
    app.include_router(breed_router)
    return app