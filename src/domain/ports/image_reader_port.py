from abc import ABC, abstractmethod

from src.domain.value_objects import ImagePath, FileContent


class ImageReaderPort(ABC):
    @abstractmethod
    def read(self, image_path: ImagePath) -> FileContent:
        pass
