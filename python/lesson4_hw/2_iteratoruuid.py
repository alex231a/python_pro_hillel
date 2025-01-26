import uuid


class IteratorUuid:
    """Class for creating unique ids."""

    def __init__(self, counter: int = 10):
        self.counter = counter

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter <= 0:
            raise StopIteration
        self.counter -= 1
        return uuid.uuid4()


if __name__ == "__main__":
    for unique_id in IteratorUuid(10):
        print(unique_id)
