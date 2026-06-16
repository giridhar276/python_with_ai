# Topic: Complex Decorators
# Example: API monitoring decorator

import time

def monitor_api(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        print("API call started:", func.__name__)

        try:
            result = func(*args, **kwargs)
            print("API call successful")
            return result
        except Exception as error:
            print("API call failed:", error)
        finally:
            end = time.time()
            print("API duration:", round(end - start, 4), "seconds")

    return wrapper

@monitor_api
def fetch_customer_profile(customer_id):
    time.sleep(1)
    return {"customer_id": customer_id, "status": "active"}

print(fetch_customer_profile("CUST1001"))
