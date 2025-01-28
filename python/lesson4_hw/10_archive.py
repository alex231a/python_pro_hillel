# Реалізуйте менеджер контексту для архівування файлів (за допомогою модуля
# zipfile). Менеджер автоматично створює архів, додає файли, а після виходу
# з блоку with – завершує архівування та закриває архів.


import zipfile
import os


class Archive:
    """Class that archives all files in a folder. Expected parameters are
    target dir and archive name"""

    def __init__(self, target_dir: str, archive_name: str):
        self.target_dir = target_dir
        self.archive_name = archive_name

    def __enter__(self):
        self.zip_ref = zipfile.ZipFile(self.archive_name, 'w',
                                       zipfile.ZIP_DEFLATED)
        for filename in os.listdir(self.target_dir):
            file_path = os.path.join(self.target_dir, filename)
            if os.path.isfile(file_path):
                self.zip_ref.write(file_path, arcname=filename)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.zip_ref:
            self.zip_ref.close()


if __name__ == '__main__':
    with Archive('.', 'archive.zip') as archive:
        print("Archived successfully!")
