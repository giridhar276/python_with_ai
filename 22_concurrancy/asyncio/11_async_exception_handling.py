"""
Asyncio Example 11: Exception Handling

Concept:
asyncio.gather(..., return_exceptions=True) captures errors as results.
"""

import asyncio


async def divide(a, b):
    await asyncio.sleep(1)
    return a / b


async def main():
    tasks = [
        divide(10, 2),
        divide(10, 0),
        divide(20, 5),
    ]

    results = await asyncio.gather(*tasks, return_exceptions=True)

    for result in results:
        if isinstance(result, Exception):
            print("Error occurred:", result)
        else:
            print("Result:", result)


asyncio.run(main())
