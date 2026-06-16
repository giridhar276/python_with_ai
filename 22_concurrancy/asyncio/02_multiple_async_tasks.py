"""
Asyncio Example 2: Multiple Async Tasks

Concept:
asyncio.gather runs multiple coroutines concurrently.
"""

import asyncio


async def download(file_name):
    print(f"Downloading {file_name}")
    await asyncio.sleep(2)
    print(f"Finished {file_name}")


async def main():
    await asyncio.gather(
        download("file1.csv"),
        download("file2.csv"),
        download("file3.csv"),
    )


asyncio.run(main())
