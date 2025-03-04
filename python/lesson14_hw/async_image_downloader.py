"""Async image downloader"""
import asyncio
from pathlib import Path

import aiohttp
from aiofiles import open as aio_open


async def download_image(session: aiohttp.ClientSession, url: str) -> None:
    """
    Downloads an image from the given URL and saves it to the specified
    filename using chunks.
    """
    downloads_dir = Path("downloads")
    downloads_dir.mkdir(exist_ok=True)
    filename = f"{Path(url).name}"
    file_path = downloads_dir / filename

    print(f"Start downloading {file_path}")
    try:
        async with session.get(url) as response:
            if response.status == 200:
                async with aio_open(file_path, 'wb') as file:
                    async for chunk in response.content.iter_chunked(1024):
                        await file.write(chunk)
                print(f"Downloaded: {file_path}")
            else:
                print(f"Failed to download {url}, status: {response.status}")
    except aiohttp.ClientPayloadError:
        print(f"Error downloading {url}: Payload issue.")


async def main():
    """
    Main function to download multiple images concurrently.
    """
    image_urls = [
        "https://mp4library.xyz/videos/scorpions-still-loving-you_265182.mp4",
        "https://dl.mp4library.xyz/videos/rauw-alejandro-baby-hello_205618"
        ".mp4",
        "https://dl.mp4library.xyz/videos/mitski-bug-like-an-angel_268519.mp4"
    ]

    async with aiohttp.ClientSession() as session:
        tasks = [download_image(session, url) for url in image_urls]
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except RuntimeError:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
