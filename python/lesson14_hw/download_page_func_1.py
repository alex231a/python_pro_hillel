"""Module with function download_page thant downloads web-pages from url"""

import asyncio
import random


async def download_page(url: str) -> None:
    """Function downloads web-pages from url"""
    print(f"Start downloading page from: {url}")
    sleep_time = random.randint(1, 5)
    await asyncio.sleep(sleep_time)
    print(f"Page from url: {url} was downloaded in {sleep_time} seconds")


async def main(urls: list) -> None:
    """Main function that downloads multiple pages concurrently"""
    tasks = [download_page(url) for url in urls]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    URLS = [
        "https://www.python.org/",
        "https://github.com/",
        "https://google.com/",
        "https://stackoverflow.com/",
        "https://docs.python.org/"
    ]


    asyncio.run(main(URLS))
