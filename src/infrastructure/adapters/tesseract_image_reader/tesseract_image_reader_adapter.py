from pathlib import Path

import pytesseract
from PIL import Image

from src.domain.ports import ImageReaderPort
from src.domain.value_objects import ImagePath, FileContent
from src.infrastructure.adapters.tesseract_image_reader.tesseract_executable_path_enum import \
    TesseractExecutablePathEnum
from src.infrastructure.exceptions import TesseractExecutablePathNotFoundException


class TesseractImageReaderAdapter(ImageReaderPort):
    __REPLACE_CHARS = {
        '\n': ' ',
        '\x0c': ' '
    }

    def __init__(self, tesseract_executable_path: TesseractExecutablePathEnum) -> None:
        self.__validate_tesseract_executable_path_exists(tesseract_executable_path)
        pytesseract.pytesseract.tesseract_cmd = tesseract_executable_path.value

    def read(self, image_path: ImagePath) -> FileContent:
        image = Image.open(image_path.value)
        raw_content = pytesseract.image_to_string(image=image, lang='por')
        raw_content_chars_replaced = self.__replace_chars(raw_content)
        return FileContent(raw_content_chars_replaced.strip())

    def __replace_chars(self, raw_content: str) -> str:
        for char in self.__REPLACE_CHARS.keys():
            raw_content = raw_content.replace(char, self.__REPLACE_CHARS[char])
        return raw_content

    @staticmethod
    def __validate_tesseract_executable_path_exists(path: TesseractExecutablePathEnum) -> None:
        if not Path(path.value).exists():
            raise TesseractExecutablePathNotFoundException(path.value)
