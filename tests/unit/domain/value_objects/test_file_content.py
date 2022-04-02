from unittest import TestCase

from src.domain.exceptions import FileContentEmptyException
from src.domain.value_objects import FileContent


class TestFileContent(TestCase):
    def test_init_WHEN_content_is_valid_THEN_creates_instance(self) -> None:
        valid_content = 'valid content'

        FileContent(valid_content)

    def test_init_WHEN_content_is_empty_THEN_raises_file_content_empty_exception(self) -> None:
        empty_content = ''

        with self.assertRaises(FileContentEmptyException):
            FileContent(empty_content)
