import logging
import time
from functools import wraps

# Set up logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Retry decorator

def retry(max_attempts=3, delay=2, exception=(Exception,)):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except exception as e:
                    attempts += 1
                    logger.warning(f'Attempt {attempts} failed: {e}')
                    if attempts == max_attempts:
                        logger.error('Max attempts reached. Operation failed.')
                        raise
                    time.sleep(delay)
                    logger.info(f'Retrying in {delay} seconds...')
        return wrapper
    return decorator

# Example network operation
@retry(max_attempts=5, delay=1, exception=(ConnectionError, TimeoutError))
def fetch_data(url):
    # Simulating a network operation
    logger.info(f'Fetching data from {url}')
    if url == 'http://fail.com':
        raise ConnectionError('Simulated connection error')
    return {'data': 'Success'}