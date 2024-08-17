import logging


class LoggingMixin:
    """
    Mixin class that provides logging functionality.

    message: The message to log.
    """

    def __init__(self):
        self.logger = logging.getLogger("__class__.__name__")
        self.logger.setLevel(logging.DEBUG)

        f_handler = logging.FileHandler(f"{self.__class__.__name__}.log")
        f_handler.setLevel(logging.INFO)
        f_format = logging.Formatter("%(asctime)s  - %(name)s - %(levelname)s - %(message)s")
        f_handler.setFormatter(f_format)

        self.logger.addHandler(f_handler)

    def log(self, message):
        self.logger.info(message)