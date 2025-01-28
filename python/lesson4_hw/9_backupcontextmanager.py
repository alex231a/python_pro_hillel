# Напишіть менеджер контексту, який буде створювати резервну копію важливого
# файлу перед його обробкою. Якщо обробка пройде успішно, оригінальний файл
# замінюється новим. У разі помилки резервна копія автоматично відновлюється.

import shutil
import os


class FileBackupManager:
    """
    Context manager that creates a backup of a file
    """

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.backup_path = file_path + '.bak'

    def __enter__(self):
        """
        Creates backup of file before processing
        """
        if os.path.exists(self.file_path):
            shutil.copy2(self.file_path, self.backup_path)
            print(f"Backup was created: {self.backup_path}")
        else:
            raise FileNotFoundError(f"File was not found: {self.file_path}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        If processing was successful changes original file with new one
        Else - restore original file
        """
        if exc_type is None:
            print("File processed successfully.")

        else:
            print(
                f"Error was occured during processing: {exc_val}. Restore "
                f"original file: {self.backup_path}.")
            shutil.copy2(self.backup_path, self.file_path)
        if os.path.exists(self.backup_path):
            os.remove(self.backup_path)
            print(f"Backup was deleted: {self.backup_path}")


if __name__ == "__main__":
    file_path = 'important_file.txt'

    with open(file_path, 'w') as f:
        f.write('This is very important information.\n')

    try:
        with FileBackupManager(file_path) as manager:
            print("Processing...")
            raise ValueError("Something went wrong.")
    except Exception as e:
        print(f"Processing was not successfully completed: {e}")
