"""Module with fetch_content function"""

import asyncio
import aiohttp


async def fetch_content(url: str) -> str:
    """Function fetch_content fetches content from given ulr"""
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return await response.text()
    except aiohttp.ClientError as error:
        return f"Error fetching {url}: {error}"
    except asyncio.TimeoutError:
        return f"Timeout error fetching {url}"
    except Exception as error:
        return f"Unexpected error fetching {url}: {error}"


async def fetch_all(urls: list) -> list:
    """Function fetches content from given list"""
    tasks = [fetch_content(url) for url in urls]
    return list(await asyncio.gather(*tasks))


async def main():
    """Main func"""
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
