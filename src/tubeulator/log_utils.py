from __future__ import annotations

import logging


class Console:
    def __init__(self, name=None, level=logging.INFO):
        self.logger = logging.getLogger(name=name)
        self.console = logging.StreamHandler()
        for target in (self.logger, self.console):
            target.setLevel(level)
        self.console.setFormatter(self.log_format)
        # If you get doubled up logs in your application, comment out the next line:
        self.logger.addHandler(self.console)

    @property
    def log_format(self) -> logging.Formatter:
        return logging.Formatter(fmt="[%(levelname)s] %(message)s")
