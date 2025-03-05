"""Module checker for async_webserver"""
import asyncio
import time

import aiohttp


async def fetch(session: aiohttp.ClientSession, url: str) -> str:
    """
    Sends a GET request to the specified URL and returns the response text.
    Handles possible exceptions to avoid crashes.
    """
    try:
        async with session.get(url, timeout=10) as response:
            return await response.text()
    except aiohttp.ClientError as error:
        return f"Error fetching {url}: {error}"
    except asyncio.TimeoutError:
        return f"Timeout error fetching {url}"
    except Exception as error:
        return f"Unexpected error fetching {url}: {error}"


async def send_requests(base_url: str) -> tuple:
    """
    Sends concurrent requests to the server and returns the responses along
    with the elapsed time.
    """
    async with aiohttp.ClientSession() as session:
        start_time = time.perf_counter()

        hello_task = fetch(session, f"{base_url}/")
        slow_task = fetch(session, f"{base_url}/slow")

        hello_response, slow_response = await asyncio.gather(hello_task,
                                                             slow_task,
                                                             return_exceptions=True)

        elapsed_time = time.perf_counter() - start_time
        return hello_response, slow_response, elapsed_time


def check_concurrent_execution(elapsed_time: float,
                               expected_time: float = 6.0) -> None:
    """
    Checks whether requests were executed concurrently.
    """
    assert elapsed_time < expected_time, ("Server is not handling requests "
                                          "concurrently!")
    print("Test passed: Server handles concurrent requests correctly.")


async def check_concurrent_requests():
    """
    Tests whether the server can handle multiple requests concurrently.
    """
    base_url = "http://localhost:8080"

    hello_response, slow_response, elapsed_time = await send_requests(base_url)

    print(f"Response from /: {hello_response}")
    print(f"Response from /slow: {slow_response}")
    print(f"Total elapsed time: {elapsed_time:.2f} seconds")

    check_concurrent_execution(elapsed_time)


if __name__ == "__main__":
    asyncio.run(check_concurrent_requests())
