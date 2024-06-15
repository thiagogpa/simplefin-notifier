import logging

def get_logger(logger_name: str = "my_logger") -> logging.Logger:
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    # Configure logger handlers and formatters
    # ...

    return logger