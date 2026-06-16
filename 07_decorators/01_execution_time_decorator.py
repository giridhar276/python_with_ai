# Topic: Decorators
# Example: Execution time decorator

import time

def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()

        # round() formats the execution duration.
        print("Execution time:", round(end - start, 4), "seconds")
    return wrapper

@timer
def generate_report():
    time.sleep(1)
    print("Report generated")

generate_report()
