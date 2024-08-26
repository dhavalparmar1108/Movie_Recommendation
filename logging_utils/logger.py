import logging

class Logger:
    def __init__(self):
        # Configure logging within the constructor
        # Use the logger
        self.logger = logging.getLogger(__name__)
        self.logger.info('MyClass instance created.')

    def log(self, msg):
        self.logger.info(msg) 