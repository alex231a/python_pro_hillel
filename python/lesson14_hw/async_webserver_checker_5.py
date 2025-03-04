"""Module checker for async_webserver"""
import asyncio
import time

import aiohttp


async def fetch(session: aiohttp.ClientSession, url: str) -> str:
    """
    Sends a GET request to the specified URL and returns the response text.
    """
    async with session.get(url) as response:
        return await response.text()


async def test_concurrent_requests():
    """
    Tests whether the server can handle multiple requests concurrently.
    """
    base_url = "http://localhost:8080"

    async with aiohttp.ClientSession() as session:
        start_time = time.time()

        # Start both requests at the same time
        hello_task = fetch(session, f"{base_url}/")
        slow_task = fetch(session, f"{base_url}/slow")

        hello_response, slow_response = await asyncio.gather(hello_task,
                                                             slow_task)

        end_time = time.time()
        elapsed_time = end_time - start_time

        print(f"Response from /: {hello_response}")
        print(f"Response from /slow: {slow_response}")
        print(f"Total elapsed time: {elapsed_time:.2f} seconds")

        # Check that the server is handling requests concurrently
        assert elapsed_time < 6, ("Server is not handling requests "
                                  "concurrently!")
        print("Test passed: Server handles concurrent requests correctly.")


if __name__ == "__main__":
    asyncio.run(test_concurrent_requests())
