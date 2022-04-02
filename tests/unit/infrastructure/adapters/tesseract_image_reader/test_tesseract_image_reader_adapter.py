from enum import Enum
from unittest import TestCase

from src.infrastructure.adapters.tesseract_image_reader import TesseractImageReaderAdapter
from src.infrastructure.adapters.tesseract_image_reader.tesseract_executable_path_enum import \
    TesseractExecutablePathEnum
from src.infrastructure.exceptions import TesseractExecutablePathNotFoundException


class TestTesseractImageReaderAdapter(TestCase):
    def test_init_WHEN_executable_path_exists_THEN_creates_instance(self) -> None:
        TesseractImageReaderAdapter(
            tesseract_executable_path=TesseractExecutablePathEnum.LINUX
        )

    def test_init_WHEN_executable_path_not_found_THEN_raises_tesseract_executable_path_not_found_exception(self) -> None:
        class FakeTesseractExecutablePathEnum(Enum):
            FAKE_PATH = 'fake_path'

        with self.assertRaises(TesseractExecutablePathNotFoundException):
            TesseractImageReaderAdapter(
                tesseract_executable_path=FakeTesseractExecutablePathEnum.FAKE_PATH
            )
