import time
import random
import requests

class NetworkError(Exception):
    pass

def retry_operation(func, max_retries=3, delay=2):
    for attempt in range(max_retries):
        try:
            return func()
        except (requests.ConnectionError, requests.Timeout) as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            time.sleep(delay)
    raise NetworkError(f"Maximum retries exceeded for {func.__name__}")

def fetch_data(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

if __name__ == '__main__':
    url = 'https://api.example.com/data'
    try:
        data = retry_operation(lambda: fetch_data(url))
        print('Data fetched successfully:', data)
    except NetworkError as ne:
        print(str(ne))