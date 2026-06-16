"""
Multiprocessing Example 14: Parallel Batch Processing

Use Case:
Process independent data batches in parallel.
"""

from concurrent.futures import ProcessPoolExecutor


def process_batch(batch):
    return {
        "batch_size": len(batch),
        "total": sum(batch),
        "average": sum(batch) / len(batch),
    }


if __name__ == "__main__":
    batches = [
        [10, 20, 30],
        [5, 15, 25, 35],
        [100, 200],
        [7, 14, 21],
    ]

    with ProcessPoolExecutor(max_workers=4) as executor:
        results = executor.map(process_batch, batches)

    for result in results:
        print(result)
