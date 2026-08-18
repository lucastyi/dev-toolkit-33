class AutoClickerException(Exception):
    """Base class for exceptions in the AutoClicker toolkit."""
    pass

class ClickLimitExceeded(AutoClickerException):
    """Exception raised when the click limit is exceeded."""
    def __init__(self, limit):
        super().__init__(f"Click limit of {limit} exceeded.")
        self.limit = limit

class InvalidClickRate(AutoClickerException):
    """Exception raised for invalid click rate settings."""
    def __init__(self, rate):
        super().__init__(f"Invalid click rate: {rate}.")
        self.rate = rate

class ClickerNotRunning(AutoClickerException):
    """Exception raised when trying to stop or modify clicker not running."""
    def __init__(self):
        super().__init__("Clicker is not currently running.")

class ConfigurationError(AutoClickerException):
    """Exception raised for configuration-related issues."""
    def __init__(self, message):
        super().__init__(f"Configuration error: {message}")
        self.message = message
