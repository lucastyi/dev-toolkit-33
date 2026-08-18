class AutoClickerError(Exception):
    """Base class for all autoclicker exceptions."""
    pass

class ClickRateError(AutoClickerError):
    """Exception raised when the click rate is invalid."""
    def __init__(self, rate):
        super().__init__(f"Invalid click rate: {rate}")
        self.rate = rate

class ConfigurationError(AutoClickerError):
    """Exception raised for configuration issues."""
    def __init__(self, message):
        super().__init__(message)

class ClickLimitExceeded(AutoClickerError):
    """Exception raised when click limit is exceeded."""
    def __init__(self, limit):
        super().__init__(f"Click limit exceeded: {limit}")
        self.limit = limit

class RuntimeError(AutoClickerError):
    """Exception raised for runtime issues in autoclicker."""
    def __init__(self, message):
        super().__init__(message)

class ClickFrequencyError(AutoClickerError):
    """Exception raised for invalid click frequency."""
    def __init__(self, frequency):
        super().__init__(f"Invalid click frequency: {frequency}")
        self.frequency = frequency

