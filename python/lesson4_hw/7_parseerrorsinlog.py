# Уявіть, що у вас є великий лог-файл від веб-сервера. Створіть генератор,
# який зчитує файл порціями (по рядку) і повертає тільки рядки з помилками (
# код статусу 4XX або 5XX). Запишіть ці помилки в окремий файл для
# подальшого аналізу.

##########################################################################
# the simpliest way is to use bash:
# grep "SOME_ERROR" path_to_file >> path_to_new_log_file
##########################################################################

class LogFileProcessor:
    """Class LogFileProcessor. Reads and returns only rows with errors"""

    def __init__(self, log_file_path: str, error_pattern: str):
        self.log_file_path = log_file_path
        self.error_pattern = error_pattern

    def error_log_generator(self):
        """
        Generator function that yields error logs
        """
        try:
            with open(self.log_file_path, 'r') as log_file:
                for line in log_file:
                    if self.error_pattern in line:
                        yield line
        except FileNotFoundError:
            print(f"File {self.log_file_path} was not found.")
            raise


class ErrorLogSaver:
    """Class ErrorLogSaver. Saves error logs"""

    def __init__(self, log_file_processor: LogFileProcessor,
                 output_file_path: str):
        self.log_file_processor = log_file_processor
        self.output_file_path = output_file_path

    def save_errors_to_file(self):
        try:
            with open(self.output_file_path, 'w') as error_file:
                for error_line in self.log_file_processor.error_log_generator():
                    error_file.write(error_line)
            print(f"Errors saved in: {self.output_file_path}")
        except Exception as e:
            print(e)


if __name__ == '__main__':
    log_processor = LogFileProcessor(log_file_path = 'test_file.txt',
                                     error_pattern = 'ERROR')
    error_saver = ErrorLogSaver(log_processor, 'errors.log')

    try:
        error_saver.save_errors_to_file()
    except Exception as e:
        print(e)