# Напишіть програму, яка використовує менеджер контексту для зчитування
# бінарних файлів великими блоками даних (наприклад, по 1024 байти).
# Виведіть кількість прочитаних байт.


class BinaryFileReader:
    """Class that reads a binary file"""

    def __init__(self, file_path: str, block_size: int = 1024):
        self.file_path = file_path
        self.block_size = block_size
        self.bytes_read = 0

    def __enter__(self):
        """Open binary file for reading"""
        self.file = open(self.file_path, 'rb')
        return self

    def __iter__(self):
        """Make iterable"""
        return self

    def __next__(self):
        """Read blocks from file"""
        data = self.file.read(self.block_size)
        if not data:
            raise StopIteration
        self.bytes_read += len(data)
        return data

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Close file"""
        if hasattr(self, 'file'):
            self.file.close()
        return False


if __name__ == '__main__':
    file_path = 'large_binary_file.bin'

    with BinaryFileReader(file_path) as reader:
        for block in reader:
            pass

        print(f"Read bytes: {reader.bytes_read}")
