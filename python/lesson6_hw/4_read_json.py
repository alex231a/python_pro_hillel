import json


class ReadJson:
    """Class reads, writes, modifies json data from file"""
    def __init__(self, file_name: str):
        self.file_name = file_name

    def _read_from_file(self):
        """Loads data from json"""
        with open(self.file_name, "r", encoding="utf-8") as f:
            content = json.load(f)
        return content

    def _write_to_file(self, content):
        """Writes to file"""
        with open(self.file_name, "w", encoding="utf-8") as f:
            json.dump(content, f, indent=4)

    def print_available_books(self):
        """Prints available books"""
        content = self._read_from_file()
        print("Available books are: ")
        print("----------------------------------------------")
        for book in content:
            if book['available']:
                for k, v in book.items():
                    print(f"{k.upper()} -- > {v}")
                print("----------------------------------------------")

    def add_new_book_in_file(self, new_book: dict):
        """Adds new book to json file"""
        try:
            content = self._read_from_file()
            if new_book in content:
                raise ValueError(
                    f"ERROR! =======> Book {new_book} already exists!")
            else:
                content.append(new_book)
                self._write_to_file(content)
        except ValueError as e:
            print(e)
        else:
            print(f"Book {new_book} was added!")


if __name__ == "__main__":
    file_name = "books.json"
    json_reader = ReadJson(file_name=file_name)

    json_reader.print_available_books()

    new_book = {"book_name": "Bookname7", "author_name": "Author8",
                "year": 2021, "available": True}

    json_reader.add_new_book_in_file(new_book)

    json_reader.print_available_books()
