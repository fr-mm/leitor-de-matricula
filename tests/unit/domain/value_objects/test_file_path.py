from unittest import TestCase

from src.domain.exceptions import FileNotFoundException
from src.domain.value_objects import ImagePath
from tests.fixtures import example_image_raw_path


class TestFilePath(TestCase):
    def test_init_WHEN_file_exists_THEN_creates_instance(self) -> None:
        ImagePath(example_image_raw_path)

    def test_init_WHEN_file_does_not_exists_THEN_raises_file_not_found_exception(self) -> None:
        fake_image_path = 'fake_image_path.jpg'

        with self.assertRaises(FileNotFoundException):
            ImagePath(fake_image_path)
