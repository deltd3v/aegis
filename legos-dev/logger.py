import datetime
import os
import logging

class AegisLogger:
    def __init__(self, log_file="aegis.log"):
        self.log_file = log_file
        self.logger = logging.getLogger("Aegis")
        self.logger.setLevel(logging.DEBUG)

        # Avoid duplicate handlers
        if not self.logger.handlers:
            # File handler
            fh = logging.FileHandler(self.log_file)
            fh.setLevel(logging.DEBUG)

            # Console handler
            ch = logging.StreamHandler()
            ch.setLevel(logging.INFO)

            # Formatter
            formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
            fh.setFormatter(formatter)
            ch.setFormatter(formatter)

            self.logger.addHandler(fh)
            self.logger.addHandler(ch)

    def log(self, message, level="INFO"):
        if level == "INFO":
            self.logger.info(message)
        elif level == "DEBUG":
            self.logger.debug(message)
        elif level == "WARNING":
            self.logger.warning(message)
        elif level == "ERROR":
            self.logger.error(message)
        elif level == "SUCCESS":
            self.logger.info(f"SUCCESS: {message}")

    def log_improvement(self, component, description):
        self.log(f"IMPROVEMENT in {component}: {description}", level="SUCCESS")

if __name__ == "__main__":
    logger = AegisLogger()
    logger.log("Logger enhanced and initialized.")
