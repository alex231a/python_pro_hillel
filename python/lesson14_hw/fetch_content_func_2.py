"""Module with fetch_content function"""

import asyncio
from typing import List

import aiohttp

SEM_LIMIT = 5


async def fetch_content(session: aiohttp.ClientSession, url: str,
                        semaphore: asyncio.Semaphore) -> str:
    """Function fetch_content fetches content from given URL using provided
    session"""
    async with semaphore:
        try:
            async with session.get(url, timeout=10) as response:
                if response.status == 200:
                    return await response.text()
                return f"Error fetching {url}: HTTP {response.status}"
        except aiohttp.ClientError as error:
            return f"Error fetching {url}: {error}"
        except asyncio.TimeoutError:
            return f"Timeout error fetching {url}"
        except Exception as error:
            return f"Unexpected error fetching {url}: {error}"


async def fetch_all(urls: List[str]) -> List[str]:
    """Function fetches content from given list using a shared session"""
    semaphore = asyncio.Semaphore(SEM_LIMIT)
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_content(session, url, semaphore) for url in urls]
        return await asyncio.gather(*tasks, return_exceptions=True)


async def main():
    """Main function"""
    urls = [
        "https://www.python.org/",
        "https://github.com/",
        "https://google.com/",
        "https://stackoverflow.com/",
        "https://docs.python.org/",
        "https://invalid-url.com/",
        "https://abrakadabra_falkadjflkmas/"
    ]

    results = await fetch_all(urls)
    for url, content in zip(urls, results):
        print(f"\n=== {url} ===\n{content[:200]}...")


asyncio.run(main())
