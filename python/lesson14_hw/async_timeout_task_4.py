"""Module which demonstrate asyncio.wait_for"""

import asyncio


async def slow_task(timeout: int) -> int:
    """Async function with timeout"""
    await asyncio.sleep(timeout)
    return 1


async def main():
    """Main function that demonstrate asyncio.wait_for"""
    task = asyncio.create_task(slow_task(5))
    try:
        result = asyncio.wait_for(task, timeout=5)
        print(await result)
    except asyncio.TimeoutError:
        print('The long task cancelled')


if __name__ == '__main__':
    asyncio.run(main())
