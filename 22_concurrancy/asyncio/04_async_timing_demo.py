"""
Asyncio Example 4: Timing Demo

Concept:
Async tasks overlap waiting time.
"""

import asyncio
import time


async def work(name, delay):
    print(f"{name} started")
    await asyncio.sleep(delay)
    print(f"{name} completed")


async def main():
    start = time.time()

    await asyncio.gather(
        work("A", 3),
        work("B", 2),
        work("C", 1),
    )

    print("Total time:", round(time.time() - start, 2), "seconds")


asyncio.run(main())
