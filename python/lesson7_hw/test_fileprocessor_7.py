"""Module with tests for FileProcessor"""

import os
import shutil
import pytest
from fileprocessor import FileProcessor


@pytest.fixture
def tmp_directory():
    """Fixture that creates tmpdir"""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    tmp_dir = os.path.join(current_dir, "tmp_dir")
    if os.path.exists(tmp_dir):
        shutil.rmtree(tmp_dir)
    os.makedirs(tmp_dir)
    return tmp_dir


def test_file_write_read(tmp_directory):
    """Test for write read file"""
    file = os.path.join(tmp_directory, "testfile.txt")
    print(file)
    FileProcessor.write_to_file(file, "Hello, World!")
    content = FileProcessor.read_from_file(str(file))
    assert content == "Hello, World!"


def test_empty_file_write_read(tmp_directory):
    """Test for empty_file_write_read"""
    file = os.path.join(tmp_directory, "testfile.txt")
    FileProcessor.write_to_file(str(file), "")
    content = FileProcessor.read_from_file(str(file))
    assert content == ""


@pytest.mark.parametrize("data", ["A" * 10000,
                                  "Sample data with \n newlines\n and tabs\t"])
def test_large_data_write_read(tmp_directory, data):
    """Test for large_data_write_read"""
    file = os.path.join(tmp_directory, "largefile.txt")
    FileProcessor.write_to_file(str(file), data)
    content = FileProcessor.read_from_file(str(file))
    assert content == data


def test_read_non_existent_file():
    """Test for read_non_existent_file"""
    with pytest.raises(FileNotFoundError,
                       match="File 'nonexistent.txt' not found."):
        FileProcessor.read_from_file("nonexistent.txt")


if __name__ == "__main__":
    pytest.main()
