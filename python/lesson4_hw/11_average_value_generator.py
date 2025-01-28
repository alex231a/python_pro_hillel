# Напишіть генератор, який по черзі зчитує великий файл даних (наприклад,
# числові показники продуктивності), обчислює середнє значення на кожній
# ітерації та оновлює результат. Це корисно для обробки великих даних,
# які не можна завантажити повністю в пам'ять.


class RunningAverage:
    """Class RunningAverage"""

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.total = 0
        self.count = 0

    def __iter__(self):
        """
        Makes object iterable
        """
        self.file = open(self.file_path, 'r')
        return self

    def __next__(self):
        """
        Method processes each line of file, count average value and add it
        to total. At the end of the file raise StopIteration
        """
        line = self.file.readline()
        if not line:
            self.file.close()
            raise StopIteration

        try:
            number = float(line.strip())
            self.total += number
            self.count += 1
            return self.total / self.count
        except ValueError:
            return self.__next__()


if __name__ == '__main__':
    file_path = 'large_data.txt'
    average_calculator = RunningAverage(file_path)
    for avg in average_calculator:
        print(f"Current average value: {avg}")
