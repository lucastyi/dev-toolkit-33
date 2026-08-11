MAX_RETRIES = 5
TIMEOUT_SECONDS = 30
SUPPORTED_FORMATS = ['json', 'xml', 'csv']
DEFAULT_LANGUAGE = 'en'
API_ENDPOINT = 'https://api.example.com/v1/'
HEADER_CONTENT_TYPE = 'application/json'
HEADER_USER_AGENT = 'DevToolkit/33.0'
ERROR_MESSAGES = {
    'invalid_input': 'The input provided is not valid.',
    'connection_failed': 'Failed to connect to the server.',
    'timeout': 'The request timed out.'
}

# Performance-related constants
CACHE_EXPIRATION = 300  # seconds
MAX_CONNECTIONS = 100
LOG_LEVEL = 'DEBUG'
DATABASE_URL = 'sqlite:///dev_toolkit.db'
