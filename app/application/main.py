from fastapi import FastAPI
from app.application.api.cat.router import router as cat_router


def create_app() -> FastAPI:
    app = FastAPI(
        title='Test'
    )
    app.include_router(cat_router)
    return app