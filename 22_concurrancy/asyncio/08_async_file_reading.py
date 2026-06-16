"""
Asyncio Example 8: Async File Reading

Concept:
aiofiles provides asynchronous file operations.

Install:
pip install aiofiles
"""

import asyncio
from pathlib import Path
import aiofiles


async def read_file(file_path):
    async with aiofiles.open(file_path, "r", encoding="utf-8") as file:
        content = await file.read()

    return file_path.name, len(content)


async def main():
    data_dir = Path(__file__).resolve().parents[1] / "data"

    files = [
        data_dir / "employees.csv",
        data_dir / "server.log",
        data_dir / "notes.txt",
    ]

    results = await asyncio.gather(*(read_file(path) for path in files))

    for file_name, size in results:
        print(file_name, "->", size, "characters")


asyncio.run(main())
