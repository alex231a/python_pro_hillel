"""Module that demonstrates speed of sending requests in different approaches
Results:

Synchronize approach: 469.31 seconds
Thread approach: 10.23 seconds
Multiprocess approach: 21.18 seconds
Async approach: 4.28 seconds

"""

import asyncio
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

import aiohttp
import requests

URL = "https://httpbin.org/delay/0.1"  # Test api with delay in 0.1 sec
REQUESTS_COUNT = 500


# Sync method
def sync_requests():
    """Function that sends requests in synchronous mode"""
    start = time.time()
    for _ in range(REQUESTS_COUNT):
        requests.get(URL, timeout=5)
    print(f"Synchronize approach: {time.time() - start:.2f} seconds")


# Thread method
def thread_request(_):
    """Function that sends request in thread mode"""
    return requests.get(URL, timeout=5)


def threaded_requests():
    """Function that sends requests in thread mode and count time"""
    start = time.time()
    with ThreadPoolExecutor(max_workers=50) as executor:
        executor.map(thread_request, range(REQUESTS_COUNT))
    print(f"Thread approach: {time.time() - start:.2f} seconds")


# Multiprocess method
def process_request(_):
    """Function that sends request in multiprocess mode"""
    return requests.get(URL, timeout=5)


def process_requests():
    """Function that sends requests in multiprocess mode and count time"""
    start = time.time()
    with ProcessPoolExecutor(max_workers=50) as executor:
        executor.map(process_request, range(REQUESTS_COUNT))
    print(f"Multiprocess approach: {time.time() - start:.2f} seconds")


# Async method
async def async_request(session):
    """Function that sends request in asynchronous mode"""
    async with session.get(URL) as response:
        return await response.text()


async def async_requests():
    """Function that sends requests in asynchronous mode and count time"""
    start = time.time()
    async with aiohttp.ClientSession() as session:
        tasks = [async_request(session) for _ in range(REQUESTS_COUNT)]
        await asyncio.gather(*tasks)
    print(f"Async approach: {time.time() - start:.2f} seconds")


if __name__ == "__main__":
    sync_requests()
    threaded_requests()
    process_requests()
    asyncio.run(async_requests())
