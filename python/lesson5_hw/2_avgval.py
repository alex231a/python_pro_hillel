class GetAvgValue:
    """Class that reads data from file and count average values if all data
    is integers"""

    def __init__(self, filename: str):
        self.filename = filename

    def _read_file(self):
        """Method for reading file"""
        with open(self.filename, 'r') as file:
            content = file.readlines()
        return content

    def get_avg_value(self):
        """Method for counting average value"""
        try:
            content = self._read_file()
            count_values = len(content)
            content = [int(val) for val in content]
            sum_values = sum(content)
            avg_val = sum_values / count_values
            return avg_val
        except ValueError as e:
            print(
                f"File contains wrong values. ({e.__class__.__name__}) - {e}")
        except FileNotFoundError as e:
            print(f"({e.__class__.__name__}) - {e}")
        except ZeroDivisionError as e:
            print(
                f"The file {self.filename} is empty. ("
                f"{e.__class__.__name__})-{e}")


if __name__ == "__main__":
    calc = GetAvgValue('empty_file.txt')
    result = calc.get_avg_value()
    if result is not None:
        print(result)
