import logging

class Logger:
    """
    A simple logger class for logging messages.
    
    Attributes:
        logger (logging.Logger): The logger instance.
    """

    def __init__(self, name: str) -> None:
        """
        Initializes Logger with a given name.
        
        Args:
            name (str): The name of the logger.
        """
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def debug(self, message: str) -> None:
        """
        Logs a debug message.
        
        Args:
            message (str): The debug message to log.
        """
        self.logger.debug(message)

    def info(self, message: str) -> None:
        """
        Logs an info message.
        
        Args:
            message (str): The info message to log.
        """
        self.logger.info(message)

    def warning(self, message: str) -> None:
        """
        Logs a warning message.
        
        Args:
            message (str): The warning message to log.
        """
        self.logger.warning(message)

    def error(self, message: str) -> None:
        """
        Logs an error message.
        
        Args:
            message (str): The error message to log.
        """
        self.logger.error(message)

    def critical(self, message: str) -> None:
        """
        Logs a critical message.
        
        Args:
            message (str): The critical message to log.
        """
        self.logger.critical(message)