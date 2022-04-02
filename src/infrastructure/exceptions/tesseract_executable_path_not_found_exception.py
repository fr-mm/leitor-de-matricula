from src.infrastructure.exceptions.infrastructure_exception import InfrastructureException


class TesseractExecutablePathNotFoundException(InfrastructureException):
    def __init__(self, tesseract_executable_path: str) -> None:
        message = f'Invalid path for Tesseract executable: {tesseract_executable_path}'
        super().__init__(message)
