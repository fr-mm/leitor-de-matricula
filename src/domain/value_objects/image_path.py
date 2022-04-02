from dataclasses import dataclass
from pathlib import Path

from src.domain.exceptions import FileNotFoundException


@dataclass(frozen=True)
class ImagePath:
    value: str

    def __post_init__(self) -> None:
        if not Path(self.value).exists():
            raise FileNotFoundException(self.value)
