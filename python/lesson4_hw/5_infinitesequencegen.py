class EvenNumberGenerator:
    """Class for Even Numbers Generating"""
    def __init__(self, start: int = 0):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise ValueError('Negative numbers are not allowed')
        if self.current == 0:
            self.current += 2
        if self.current % 2 != 0:
            self.current += 1
        even_number = self.current
        self.current += 2
        return even_number


class LimitGeneratorContext:
    """Context manager for limiting length of sequence"""
    def __init__(self, generator: EvenNumberGenerator, f_name:str, limit:int = 100):
        self.generator = generator
        self.limit = limit
        self.filename = f_name
        self.count = 0  # Count of generated numbers

    def __enter__(self):
        self.file = open(self.filename, 'w')
        return self  # Return the context manager, not the generator

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        return False  # Let any exceptions propagate

    def write_to_file(self, number):
        """Method for writing number to file"""
        if self.count <= self.limit:
            self.file.write(f"{number}\n")
            self.count += 1
            return True  # Allow the loop to continue if count <= limit
        return False  # Stop iteration if count reaches limit


if __name__ == "__main__":

    filename = 'even_numbers.txt'
    even_gen = EvenNumberGenerator()

    with LimitGeneratorContext(even_gen, filename, 100) as context:
        for even_number in even_gen:
            if not context.write_to_file(even_number):
                break  # Stop the loop after writing 100 numbers

    print("100 even numbers have been written to 'even_numbers.txt'.")
