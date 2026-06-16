"""
Asyncio Example 10: Timeout

Concept:
asyncio.wait_for cancels a task if it takes too long.
"""

import asyncio


async def slow_api_call():
    await asyncio.sleep(5)
    return "API response received"


async def main():
    try:
        result = await asyncio.wait_for(slow_api_call(), timeout=2)
        print(result)
    except asyncio.TimeoutError:
        print("The API call took too long and was cancelled")


asyncio.run(main())
