"""Module with class FileProcessor"""
import os


class FileProcessor:
    """Class File Processor"""

    @staticmethod
    def write_to_file(file_path: str, data: str):
        """
        Write data to a file.
        :param file_path: Path to the file
        :param data: String data to write to the file
        """
        with open(file_path, 'w', encoding="utf-8") as file:
            file.write(data)

    @staticmethod
    def read_from_file(file_path: str) -> str:
        """
        Read data from a file.
        :param file_path: Path to the file
        :return: Content of the file as a string
        :raises FileNotFoundError: If the file does not exist
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File '{file_path}' not found.")

        with open(file_path, 'r', encoding="utf-8") as file:
            return file.read()
