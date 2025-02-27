"""Module with functions than analyze files"""
import os
import threading

print_lock = threading.Lock()

def get_information_from_file(file_path: str, find_pattern: str) -> None:
    """Function to analyze single file"""
    lock_path = file_path + ".lock"

    try:
        file_descriptor = os.open(lock_path, os.O_CREAT | os.O_EXCL)
        os.close(file_descriptor)
    except FileExistsError:
        return

    result_list = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                if find_pattern in line:
                    result_list.append(line.strip())

        with print_lock:
            print(
                f"In file {file_path} found {len(result_list)} lines with pattern {find_pattern}")
            print(result_list)

    except UnicodeDecodeError:
        with print_lock:
            print(f"[!] Encoding error while reading {file_path}")

    except FileNotFoundError:
        with print_lock:
            print(f"[!] File not found: {file_path}")

    finally:
        os.remove(lock_path)

def analyze_files(target_dir: str, find_pattern: str) -> None:
    """Function to analyze many files with many threads"""
    files = os.listdir(target_dir)
    collect_threads = []
    for file in files:
        file_path = os.path.join(target_dir, file)
        if not os.path.isfile(file_path):
            continue

        thread = threading.Thread(target=get_information_from_file,
                                  args=(file_path, find_pattern))
        collect_threads.append(thread)
        thread.start()

    for thread in collect_threads:
        thread.join()


if __name__ == '__main__':
    LOG_PATH = 'analyzed_logs'
    PATTERN = "WARNING"

    analyze_files(LOG_PATH, PATTERN)
