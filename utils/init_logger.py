import logging
from typing import Optional
from utils.logger import get_logger


def init_logger(logger_name: str = "my_logger", file_logging_level: Optional[str] = None) -> logging.Logger:
    logger = get_logger(logger_name)

    # Create a console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    # Create log formatters
    console_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

    # Set formatters for the handler
    console_handler.setFormatter(console_formatter)

    # Add the console handler to the logger
    logger.addHandler(console_handler)

    # Add file handlers if file_logging_level is provided
    if file_logging_level:
        file_handler = logging.FileHandler(f"{logger_name}.log")
        file_handler.setLevel(logging.getLevelName(file_logging_level))
        file_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)

    return logger

app_logger = init_logger()