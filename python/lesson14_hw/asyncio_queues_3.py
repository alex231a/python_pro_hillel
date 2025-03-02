"""Asynchronous task queue implementation using asyncio.Queue"""

import asyncio


async def producer(queue: asyncio.Queue) -> None:
    """Producer Function"""
    for i in range(1, 6):
        await queue.put(i)
        print(f"Producer add task number {i} to queue")
        await asyncio.sleep(1)


async def consumer(queue: asyncio.Queue) -> None:
    """Consumer Function"""
    while True:
        task = await queue.get()
        print(f"Consumer processing task number {task}")
        await asyncio.sleep(2)
        print(f"Consumer finished task number {task}")
        queue.task_done()


async def main():
    """Main function"""
    queue = asyncio.Queue()
    producer_task = asyncio.create_task(producer(queue))
    consumer_tasks = [asyncio.create_task(consumer(queue)) for _ in range(3)]
    await producer_task
    await queue.join()

    for cans_l in consumer_tasks:
        cans_l.cancel()

    await asyncio.gather(*consumer_tasks, return_exceptions=True)


if __name__ == "__main__":
    asyncio.run(main())
