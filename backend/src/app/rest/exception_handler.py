from fastapi import FastAPI
from httpx import Request
from starlette.responses import JSONResponse

from app.shared.exception.domain_exception import DomainException
from app.shared.exception.not_found_exception import NotFoundException


def validation_exception_handler(request: Request, exception: DomainException):
    if isinstance(exception, NotFoundException):
        return build_response(404, exception)


def build_response(status_code: int, exception: DomainException):
    return JSONResponse(status_code=status_code, content={
        'title': exception.code,
        'status': status_code,
        'detail': exception.details
    })


def add_exception_handler(app: FastAPI):
    app.add_exception_handler(DomainException, validation_exception_handler)
