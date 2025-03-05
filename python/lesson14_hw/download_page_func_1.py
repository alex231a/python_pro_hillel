"""Module with function download_page thant downloads web-pages from url"""

import asyncio
import logging
import random
from typing import List

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")


async def download_page(url: str) -> None:
    """Simulates downloading a web page with random delay and error handling"""

    retries = 3
    for attempt in range(1, retries + 1):
        try:
            print(f"Start downloading page from: {url}")
            sleep_time = random.randint(1, 5)
            await asyncio.sleep(sleep_time)

            if random.random() < 0.2:
                raise TimeoutError("Simulated timeout error")

            print(
                f"Page from url: {url} was downloaded in {sleep_time} seconds")
            return
        except TimeoutError as error:
            logging.warning("Attempt %d failed for %s: %s", attempt, url,
                            error)
            if attempt == retries:
                logging.error("Failed to download %s after %d attempts", url,
                              retries)


async def main(urls: List[str]) -> None:
    """Main function that downloads multiple pages concurrently"""
    tasks = [download_page(url) for url in urls]
    await asyncio.gather(*tasks, return_exceptions=True)


if __name__ == "__main__":
    URLS = [
        "https://www.python.org/",
        "https://github.com/",
        "https://google.com/",
        "https://stackoverflow.com/",
        "https://docs.python.org/"
    ]

    asyncio.run(main(URLS))
