"""Module with functions than analyze files"""
import os
import threading


def get_information_from_file(file_path: str, find_pattern: str) -> None:
    """Function to analyze single file"""
    result_list = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if find_pattern in line:
                result_list.append(line.strip())
    print(
        f"In file {file_path} found {len(result_list)} lines with pattern "
        f"{find_pattern}")
    print(result_list)


def analyze_files(target_dir: str, find_pattern: str) -> None:
    """Function to analyze many files with many threads"""
    files = os.listdir(target_dir)
    collect_threads = []
    for file in files:
        file_path = os.path.join(target_dir, file)
        thread = threading.Thread(target=get_information_from_file,
                                  args=(file_path, find_pattern))
        collect_threads.append(thread)
        thread.start()
    for thread in collect_threads:
        thread.join()


if __name__ == '__main__':
    LOG_PATH = 'logs'
    PATTERN = "WARNING"

    analyze_files(LOG_PATH, PATTERN)
