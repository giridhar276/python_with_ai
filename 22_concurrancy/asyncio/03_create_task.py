"""
Asyncio Example 3: create_task

Concept:
asyncio.create_task schedules a coroutine to run in the background.
"""

import asyncio


async def task(name):
    print(f"{name} started")
    await asyncio.sleep(1)
    print(f"{name} completed")


async def main():
    task1 = asyncio.create_task(task("Task 1"))
    task2 = asyncio.create_task(task("Task 2"))

    await task1
    await task2


asyncio.run(main())
