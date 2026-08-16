# logger.py
import logging

# Configure the logger
def configure_logger(name: str) -> logging.Logger:
    """
    Configure a logger with the specified name.
    
    Args:
        name: The name of the logger. Used for distinguishing different loggers.
    
    Returns:
        A configured logger instance.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

# Example usage
if __name__ == '__main__':
    logger = configure_logger('AutoClicker')
    logger.info('Logger is configured and ready.')
    logger.debug('This is a debug message.')
    logger.error('This is an error message.')
