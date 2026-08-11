import re

class ValidationError(Exception):
    pass

def validate_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not isinstance(email, str):
        raise ValidationError('Email must be a string')
    if not re.match(email_regex, email):
        raise ValidationError('Invalid email format')
    return True


def validate_age(age):
    if not isinstance(age, int):
        raise ValidationError('Age must be an integer')
    if age < 0:
        raise ValidationError('Age cannot be negative')
    if age > 120:
        raise ValidationError('Age is unrealistically high')
    return True


def validate_username(username):
    if not isinstance(username, str):
        raise ValidationError('Username must be a string')
    if not (3 <= len(username) <= 30):
        raise ValidationError('Username must be between 3 and 30 characters')
    if not username.isalnum():
        raise ValidationError('Username must be alphanumeric')
    return True
