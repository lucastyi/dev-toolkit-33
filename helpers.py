import time
import requests
from functools import wraps


def retry_operation(max_retries=3, delay=2):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < max_retries:
                try:
                    return func(*args, **kwargs)
                except requests.RequestException as e:
                    print(f'Attempt {retries + 1} failed: {e}')
                    retries += 1
                    time.sleep(delay)
            raise Exception(f'Failed after {max_retries} attempts')
        return wrapper
    return decorator


@retry_operation(max_retries=5, delay=3)
def fetch_data(url):
    response = requests.get(url)
    response.raise_for_status()  # Raise HTTPError for bad responses
    return response.json()


if __name__ == '__main__':
    data = fetch_data('https://api.example.com/data')
    print(data)