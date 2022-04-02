from dataclasses import dataclass
from pathlib import Path

from src.domain.exceptions import FileNotFoundException
from src.domain.exceptions.invalid_file_suffix_exception import InvalidFileSuffixException


VALID_SUFFIXES = [
    'png',
    'jpg'
]


@dataclass(frozen=True)
class ImagePath:
    value: str

    def __post_init__(self) -> None:
        self.__validate_path_exists()
        self.__validate_suffix()

    def __validate_path_exists(self) -> None:
        if not Path(self.value).exists():
            raise FileNotFoundException(self.value)

    def __validate_suffix(self) -> None:
        suffix = self.value.split('.')[-1]
        if suffix not in VALID_SUFFIXES:
            raise InvalidFileSuffixException(
                file_name=self.value,
                valid_suffixes=VALID_SUFFIXES
            )
