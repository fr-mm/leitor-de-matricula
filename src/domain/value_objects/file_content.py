from dataclasses import dataclass

from src.domain.exceptions import FileContentEmptyException


@dataclass(frozen=True)
class FileContent:
    value: str

    def __post_init__(self) -> None:
        self.__validate_not_empty()

    def __validate_not_empty(self) -> None:
        if not self.value:
            raise FileContentEmptyException()
