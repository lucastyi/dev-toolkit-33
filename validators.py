import re

class InputValidator:
    @staticmethod
    def validate_email(email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(pattern, email):
            return True
        return False

    @staticmethod
    def validate_phone(phone):
        pattern = r'^\+?[1-9]\d{1,14}$'
        if re.match(pattern, phone):
            return True
        return False

    @staticmethod
    def validate_username(username):
        pattern = r'^[a-zA-Z0-9_]{3,30}$'
        if re.match(pattern, username):
            return True
        return False

    @staticmethod
    def validate_password(password):
        if len(password) < 8:
            return False
        if not re.search(r'[A-Z]', password):
            return False
        if not re.search(r'[a-z]', password):
            return False
        if not re.search(r'[0-9]', password):
            return False
        return True

# Example usage:
# validator = InputValidator()
# is_valid_email = validator.validate_email('test@example.com')  # Returns True
# is_valid_phone = validator.validate_phone('+123456789012')  # Returns True
# is_valid_username = validator.validate_username('user_name')  # Returns True
# is_valid_password = validator.validate_password('Password1')  # Returns True
