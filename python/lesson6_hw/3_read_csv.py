import csv


class CustomCsvRW:
    """Class that reads csv, prints it, adds new information"""

    def __init__(self, file_name: str):
        self.file_name = file_name

    def read_csv(self):
        """Reads csv"""
        with open(self.file_name, mode='r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            headers = next(reader)
            print(" ".join(headers))
            for row in reader:
                print(" ".join(row))

    def get_average_mark(self):
        """Gets average marks"""
        with open(self.file_name, mode='r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            count_mark = 0
            count_iter = 0
            for row in reader:
                count_mark += int(row['Mark'])
                count_iter += 1
            avg_val = count_mark / count_iter
            print(f"Average mark is {avg_val}")

    def add_new_student(self, new_student: list):
        """Adds new student to csv"""
        new_content = []
        try:
            with open(self.file_name, mode='r', newline='',
                      encoding='utf-8') as f:
                reader = csv.reader(f)
                for row in reader:
                    if new_student == row:
                        raise ValueError(
                            f"Student {new_student} already exists.")
                    new_content.append(row)
            new_content.append(new_student)

            with open(self.file_name, mode='w', newline='',
                      encoding='utf-8') as f:
                writer = csv.writer(f)
                for row in new_content:
                    writer.writerow(row)

        except ValueError as e:
            print(f'An error occurred while reading the file. {e}.')
        except Exception as e:
            print(f'An error occurred while writing new content to file. {e}.')
        else:
            print(f"New student {new_student} was added to .csv file")


if __name__ == "__main__":
    file_name = "students.csv"
    file_csv = CustomCsvRW(file_name)

    file_csv.read_csv()
    print("------------------------")
    file_csv.get_average_mark()
    print("------------------------")
    new_student = ["Bob", '30', '98']
    file_csv.add_new_student(new_student)
    print("------------------------")
    file_csv.read_csv()
    print("------------------------")
