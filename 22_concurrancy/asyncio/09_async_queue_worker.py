"""
Asyncio Example 9: Async Queue Worker

Concept:
asyncio.Queue is used for async producer-consumer workflows.
"""

import asyncio


async def worker(worker_name, queue):
    while True:
        task = await queue.get()

        if task is None:
            queue.task_done()
            print(worker_name, "stopped")
            break

        print(worker_name, "processing", task)
        await asyncio.sleep(1)
        queue.task_done()


async def main():
    queue = asyncio.Queue()

    workers = [
        asyncio.create_task(worker(f"Worker-{i}", queue))
        for i in range(1, 4)
    ]

    for task_id in range(1, 8):
        await queue.put(f"Task-{task_id}")

    await queue.join()

    for _ in workers:
        await queue.put(None)

    await asyncio.gather(*workers)


asyncio.run(main())
