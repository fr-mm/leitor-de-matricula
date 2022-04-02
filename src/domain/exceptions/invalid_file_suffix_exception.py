from src.domain.exceptions import DomainException


class InvalidFileSuffixException(DomainException):
    def __init__(self, file_name: str, valid_suffixes: [str]) -> None:
        message = f'{file_name}\n Valid suffixes: {valid_suffixes}'
        super().__init__(message)
