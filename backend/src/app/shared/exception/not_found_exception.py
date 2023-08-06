from app.shared.exception.domain_exception import DomainException


class NotFoundException(DomainException):

    def __init__(self, details: str):
        super().__init__("NOT_FOUND", details)
