import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def is_positive_integer(value):
    if isinstance(value, int) and value > 0:
        return True
    return False


def is_string_non_empty(s):
    return isinstance(s, str) and bool(s)


def is_valid_click_interval(interval):
    return isinstance(interval, (int, float)) and interval > 0


def validate_settings(settings):
    if not is_valid_email(settings.get('email')):
        raise ValueError('Invalid email format')
    if not is_positive_integer(settings.get('click_count', 0)):
        raise ValueError('Click count must be a positive integer')
    if not is_valid_click_interval(settings.get('click_interval')):
        raise ValueError('Click interval must be a positive number')
    if not is_string_non_empty(settings.get('user_agent')):
        raise ValueError('User agent cannot be empty')