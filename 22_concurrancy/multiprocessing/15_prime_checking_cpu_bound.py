"""
Multiprocessing Example 15: Prime Checking

CPU-bound Use Case:
Checking whether large numbers are prime.
"""

from concurrent.futures import ProcessPoolExecutor


def is_prime(number):
    if number < 2:
        return number, False

    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return number, False

    return number, True


if __name__ == "__main__":
    numbers = [999983, 999979, 999961, 999959, 1000000]

    with ProcessPoolExecutor(max_workers=4) as executor:
        results = executor.map(is_prime, numbers)

    for number, result in results:
        print(number, "is prime?", result)
