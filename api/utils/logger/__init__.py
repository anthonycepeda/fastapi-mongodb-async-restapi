import logging
import os


def logger_config(module):
    """
    LOGGER function. Extends Python loggin module and set a custom config.
    params: Module name to __name__ magic method.
    return: Logger object
    usage: logger_config(__name__)
    """
    formatter = logging.Formatter("%(asctime)s [%(levelname)s] [%(message)s]")

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    logger = logging.getLogger(module)
    logger.setLevel(os.getenv("LOG_LEVEL", "DEBUG"))
    logger.addHandler(handler)

    return logger
