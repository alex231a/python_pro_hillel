# Напишіть ітератор, який буде повертати всі файли в заданому каталозі по
# черзі. Для кожного файлу виведіть його назву та розмір.

import os


class FileIterator:
    """Class iterator for getting and describing all files in a directory."""
    def __init__(self, target_dir: str):
        self.target_dir = target_dir
        self.file_list = []
        self.index = 0

    def __iter__(self):
        self.file_list = [f for f in os.listdir(self.target_dir) if
                          os.path.isfile(os.path.join(self.target_dir, f))]
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.file_list):
            raise StopIteration
        filename = self.file_list[self.index]
        full_path = os.path.join(self.target_dir, filename)
        file_size = os.path.getsize(full_path)
        self.index += 1
        return filename, file_size


if __name__ == '__main__':
    target_dir = ('D:\PYTHON_STYDYING\hillel\python_pro_hillel\python'
                  '\lesson4_hw')
    file_iterator = FileIterator(target_dir)
    for file_name, file_size in file_iterator:
        print(f"File name is: {file_name}, file size is: {file_size}")
