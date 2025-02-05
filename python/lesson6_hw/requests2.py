"""Module that demonstarates requests"""

import requests


def get_content_and_save_in_file(url_send: str, file_name: str):
    """Function that gets html content from the web-page and save it if file"""
    try:
        content = requests.get(url_send, timeout=5).text
        with open(file_name, 'w', encoding="utf-8") as file:
            file.write(content)
        print(
            f"HTML content of page {url_send} was successfully saved in "
            f"{file_name}")
    except requests.exceptions.ConnectionError as err:
        print(f"ERROR. Web page is unreachable! {err}")


if __name__ == "__main__":
    URL = "https://google.com/"
    FILE_NAME = "web_content.txt"

    get_content_and_save_in_file(URL, FILE_NAME)
