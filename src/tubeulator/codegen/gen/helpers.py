import logging
from textwrap import indent

__all__ = ["logger"]

logger = logging.getLogger("tubeulator.codegen.gen")


class CustomFormatter(logging.Formatter):
    def formatException(self, exc_info):
        result = super().formatException(exc_info)
        return indent(
            f"\n{result}\n",
            prefix=" " * 8,
        )


formatter = CustomFormatter("[%(levelname)s] - %(message)s")

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)
