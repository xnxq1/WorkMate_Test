from functools import partial
from typing import Callable, Awaitable

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import ORJSONResponse
from pydantic import ValidationError
from app.application.schemas import ErrorResponse
from app.domain.exceptions import BaseAppException
from app.infra.db.repo.exceptions import BaseRepoException, NotCatException, NotCatsWithThisBreedException, \
    NotBreedWithThisNameException


def register_exceptions(app: FastAPI):
    app.add_exception_handler(BaseRepoException, partial_handler(500))
    app.add_exception_handler(BaseAppException, partial_handler(500))
    app.add_exception_handler(NotCatException, partial_handler(400))
    app.add_exception_handler(NotCatsWithThisBreedException, partial_handler(400))
    app.add_exception_handler(RequestValidationError, pydantic_handler)


def partial_handler(status_code: int) -> Callable[..., Awaitable[ORJSONResponse]]:
    return partial(exception_handler, status_code=status_code)


def exception_handler(request: Request, exc: BaseAppException, status_code: int) -> ORJSONResponse:
    return ORJSONResponse(
        content=ErrorResponse(status=status_code, error=exc.message),
        status_code=status_code,

    )


def pydantic_handler(request: Request, exc: RequestValidationError) -> ORJSONResponse:
    errors = exc.errors()
    errors = [error['msg'] for error in errors]
    return ORJSONResponse(
        content=ErrorResponse(status=422, error=errors),
        status_code=422,
    )