"""Module with function download_file"""
import os
import random
import threading

import requests


def download_file(url: str) -> None:
    """Function to download file from url"""
    filename = f"{random.randint(1, 100)}{os.path.basename(url)}"
    file_path = os.path.join("downloads", filename)
    print(f"Start downloading {filename}")
    response = requests.get(url, timeout=20)
    with open(file_path, "wb") as file:
        file.write(response.content)
    print(f"Downloaded {filename} to {file_path}")


if __name__ == "__main__":
    URL = "https://mp4library.xyz/videos/scorpions-still-loving-you_265182.mp4"

    thread1 = threading.Thread(target=download_file, args=(URL,))
    thread2 = threading.Thread(target=download_file, args=(URL,))
    thread3 = threading.Thread(target=download_file, args=(URL,))

    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()
