import requests


def get_content_and_save_in_file(url: str, file_name: str):
    """Function that gets html content from the web-page and save it if file"""
    try:
        content = requests.get(url).text
        with open(file_name, 'w') as f:
            f.write(content)
        print(
            f"HTML content of page {url} was successfully saved in "
            f"{file_name}")
    except requests.exceptions.ConnectionError as e:
        print(f"ERROR. Web page is unreachable! {e}")


if __name__ == "__main__":
    url = "https://google.com/"
    file_name = "web_content.txt"

    get_content_and_save_in_file(url, file_name)
