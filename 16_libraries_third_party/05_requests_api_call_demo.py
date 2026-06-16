# Topic: Third-party Libraries
# Example: API call using requests

try:
    import requests
except ImportError:
    print("Please install requests: pip install requests")
    raise SystemExit

url = "https://httpbin.org/get"

try:
    # requests.get() sends HTTP GET request.
    response = requests.get(url, timeout=5)
    print(response.status_code)
    print(response.json().keys())
except requests.RequestException as error:
    print("API call failed:", error)
