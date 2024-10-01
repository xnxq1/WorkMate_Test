from fastapi import FastAPI



def create_app() -> FastAPI:
    app = FastAPI(
        title='Test'
    )
    return app