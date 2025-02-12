"""Module with function that removes urls from text"""
import re


def remove_url_from_text(txt: str) -> str:
    """Function that removes urls from text"""
    pattern = (r"(?:http|ftp|https):\/\/[\w_-]+(?:\.[\w_-]+)+(?:[\w.,"
               r"@?^=%&:/~+#-]*)")
    result = re.findall(pattern, txt)
    print(f"Next urls will be removed from text:\n{result}")
    new_txt = re.sub(pattern, '', txt)
    new_txt = re.sub(r'""', '', new_txt)
    new_txt = re.sub(r'\s+', ' ', new_txt).strip()
    return new_txt


if __name__ == "__main__":
    TEXT = """
    some_text
    https://www.example.com,
    http://example.org,
    https://subdomain.example.net/path/to/page,
    "http://www.example.com?query=123&sort=asc",
    "https://example.com:8080",
    example1,
    "ftp://ftp.example.com/files",
    "http://192.168.1.1",
    "https://example.com#section",
    "https://www.example.com/blog/article?id=42"
    end of text
    """

    print(remove_url_from_text(TEXT))
