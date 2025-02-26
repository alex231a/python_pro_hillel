"""Module with function download_file"""
import os
import random
import threading

import requests


def download_file(url: str) -> None:
    """Function to download file from url"""
    filename = f"{random.randint(1, 100)}{os.path.basename(url)}"
    file_path = os.path.join("downloads", filename)
    print(f"{threading.current_thread().name}. Start downloading {filename}")
    response = requests.get(url, timeout=20)
    with open(file_path, "wb") as file:
        file.write(response.content)
    print(
        f"{threading.current_thread().name}. Downloaded {filename} to "
        f"{file_path}")


if __name__ == "__main__":
    URL = "https://mp4library.xyz/videos/scorpions-still-loving-you_265182.mp4"

    thread1 = threading.Thread(target=download_file, args=(URL,),
                               name="download_thread1")
    thread2 = threading.Thread(target=download_file, args=(URL,),
                               name="download_thread2")
    thread3 = threading.Thread(target=download_file, args=(URL,),
                               name="download_thread3")

    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()
