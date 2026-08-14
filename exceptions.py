class AutoClickerError(Exception):
    """Base class for exceptions in the AutoClicker application."""
    pass

class InvalidClickFrequencyError(AutoClickerError):
    """Exception raised for invalid click frequency values."""
    def __init__(self, frequency):
        self.frequency = frequency
        super().__init__(f"Invalid click frequency: {frequency}")

class ClickRateLimitExceededError(AutoClickerError):
    """Exception raised when click rate limit is exceeded."""
    def __init__(self, limit):
        self.limit = limit
        super().__init__(f"Click rate limit exceeded: {limit} clicks per second")

class ClickTargetNotFoundError(AutoClickerError):
    """Exception raised when the target for clicking is not found."""
    def __init__(self, target):
        self.target = target
        super().__init__(f"Click target not found: {target}")

class InitializationError(AutoClickerError):
    """Exception raised during the initialization of the auto-clicker."""
    def __init__(self, message):
        super().__init__(message)

