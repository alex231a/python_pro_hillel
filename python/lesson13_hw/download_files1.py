"""Module with function download_file"""
# import os
import threading
import uuid
from pathlib import Path

import requests


def download_file(url_inp: str) -> None:
    """Function to download file from url"""
    # Ensure downloads directory exists
    downloads_dir = Path("downloads")
    downloads_dir.mkdir(exist_ok=True)

    # Generate a unique filename
    filename = f"{uuid.uuid4()}_{Path(url).name}"
    file_path = downloads_dir / filename

    print(f"{threading.current_thread().name}. Start downloading {filename}")

    try:
        with requests.get(url_inp, stream=True, timeout=20) as response:
            response.raise_for_status()
            with open(file_path, "wb") as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
        print(
            f"{threading.current_thread().name}: Downloaded {filename} to "
            f"{file_path}")
    except requests.RequestException as error:
        print(
            f"{threading.current_thread().name}: Failed to download "
            f"{url_inp} - {error}")
    except OSError as error:
        print(f"{threading.current_thread().name}: File write error - {error}")


if __name__ == "__main__":
    URLS = [
        "https://mp4library.xyz/videos/scorpions-still-loving-you_265182.mp4",
        "https://dl.mp4library.xyz/videos/rauw-alejandro-baby-hello_205618"
        ".mp4",
        "https://dl.mp4library.xyz/videos/mitski-bug-like-an-angel_268519.mp4"
    ]

    threads = []
    for i, url in enumerate(URLS, start=1):
        thread = threading.Thread(target=download_file, args=(url,),
                                  name=f"download_thread{i}")
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
