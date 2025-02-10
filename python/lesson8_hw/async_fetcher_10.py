"""Docstring module"""
import asyncio
from typing import Dict, Any


# Suppress the pylint warning for too few public methods
# pylint: disable=R0903


class AsyncFetcher:
    """Class AsyncFetcher"""

    @staticmethod
    async def fetch(url: str) -> Dict[str, Any]:
        """Method fetch"""
        await asyncio.sleep(1)
        return {"result_code": 200, "url": f"{url}",
                "data": "information_fetched"}


if __name__ == "__main__":
    async def main():
        """main func"""
        fetcher = AsyncFetcher()
        result = await fetcher.fetch("https://example.com/api")
        print(result)


    asyncio.run(main())
