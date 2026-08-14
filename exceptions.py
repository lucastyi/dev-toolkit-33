class AutoClickerError(Exception):
    """Base class for all exceptions raised by the autoclicker."""

class ClickRateError(AutoClickerError):
    """Raised when click rate is invalid."""
    def __init__(self, rate):
        self.rate = rate
        super().__init__(f'Invalid click rate: {rate}')

class ConfigurationError(AutoClickerError):
    """Raised when configuration is incorrect."""
    def __init__(self, message):
        super().__init__(f'Configuration error: {message}')

class ClickLimitExceeded(AutoClickerError):
    """Raised when click limit is exceeded."""
    def __init__(self, limit):
        self.limit = limit
        super().__init__(f'Click limit exceeded: {limit}')