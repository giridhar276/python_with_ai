"""
Asyncio Example 1: Basic Async Function

Concept:
async defines a coroutine.
await pauses the coroutine without blocking the entire program.
"""

import asyncio


async def main():
    print("Async function started")

    # asyncio.sleep is non-blocking.
    await asyncio.sleep(1)

    print("Async function completed")


asyncio.run(main())
