class ReverseFileIterator:
    """Class for reading file from end to beginning."""

    def __init__(self, filename: str):
        self.filename = filename
        self.lines = None
        self.index = None

    def __iter__(self):
        """Method for iterating."""
        with open(self.filename, encoding="utf-8") as f:
            self.lines = f.readlines()[::-1]
        self.index = 0
        return self

    def __next__(self):
        """Method for next."""
        if self.index is None or self.index >= len(self.lines):
            raise StopIteration
        line = self.lines[self.index].strip()
        self.index += 1
        return line


if __name__ == "__main__":
    for line in ReverseFileIterator("test_file.txt"):
        print(line)
