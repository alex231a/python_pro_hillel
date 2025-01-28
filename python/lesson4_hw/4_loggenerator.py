# Реалізуйте генератор, який читає великий текстовий файл рядок за рядком
# (наприклад, лог-файл) і повертає лише ті рядки, що містять певне ключове
# слово.
# Використайте цей генератор для фільтрації файлу та запису відповідних
# рядків у новий файл.


class ReadFileFilter:
    """Class ReadFileFilter creates generator with filter"""

    def __init__(self, filename: str, search_pattern: str):
        self.filename = filename
        self.search_pattern = search_pattern

    def __iter__(self):
        with open(self.filename, encoding="utf-8") as f:
            for line in f:
                if self.search_pattern in line:
                    yield line


def save_filtered(log_file: str, filtered_log_file: str, search_pattern: str):
    """Function saves filtered log file"""
    reader = ReadFileFilter(log_file, search_pattern)
    with open(filtered_log_file, "w", encoding="utf-8") as f:
        for line in reader:
            f.write(line)


if __name__ == "__main__":
    save_filtered("test_file.txt", "filtered_logs.txt", "ERROR")
