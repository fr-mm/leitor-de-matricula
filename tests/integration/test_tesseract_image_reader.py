from unittest import TestCase

from src.domain.value_objects import ImagePath, FileContent
from src.infrastructure.adapters.tesseract_image_reader import TesseractImageReaderAdapter
from src.infrastructure.adapters.tesseract_image_reader.tesseract_executable_path_enum import \
    TesseractExecutablePathEnum
from tests.fixtures import simple_image_example_raw_path


class TestTesseractImageReader(TestCase):
    def test_read_WHEN_image_has_text_THEN_returns_file_content_with_image_text(self) -> None:
        image_path = ImagePath(simple_image_example_raw_path)
        tesseract_image_reader = TesseractImageReaderAdapter(
            tesseract_executable_path=TesseractExecutablePathEnum.LINUX
        )

        actual_file_content = tesseract_image_reader.read(image_path)

        expected_file_content = FileContent('Abc 123')
        self.assertEqual(expected_file_content, actual_file_content)
