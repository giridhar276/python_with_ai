"""
Threading Example 15: Download Multiple Files

Real-time Use Case:
Download images or files concurrently.

Install:
pip install requests
"""

from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import requests


output_dir = Path(__file__).resolve().parent / "downloads"
output_dir.mkdir(exist_ok=True)

urls = [
    "https://httpbin.org/image/png",
    "https://httpbin.org/image/jpeg",
    "https://httpbin.org/image/webp",
]


def download_file(index_and_url):
    index, url = index_and_url

    response = requests.get(url, timeout=10)

    # Save response content as binary file.
    file_path = output_dir / f"downloaded_file_{index}.bin"
    file_path.write_bytes(response.content)

    return file_path


with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(download_file, enumerate(urls, start=1))

for file_path in results:
    print("Downloaded:", file_path)
