import time
import requests

class NetworkOperationError(Exception):
    pass

def retry_request(url, max_retries=3, delay=2):
    retries = 0
    while retries < max_retries:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raises an HTTPError for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            retries += 1
            if retries == max_retries:
                raise NetworkOperationError(f'Failed to fetch {url} after {max_retries} retries') from e
            time.sleep(delay)

# Example usage:
if __name__ == '__main__':
    url = 'https://api.example.com/data'
    try:
        result = retry_request(url)
        print(result)
    except NetworkOperationError as e:
        print(e)