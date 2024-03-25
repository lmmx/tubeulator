from __future__ import annotations

import subprocess
from contextlib import AbstractContextManager
from dataclasses import dataclass

from ..utils.logs import set_up_logging
from ..utils.paths import db_path

__all__ = [
    "start_mongod",
    "MongodProcess",
    "get_mongod_process",
    "MongodExceptionGuard",
]

logger = set_up_logging(__name__)


def start_mongod() -> None:
    db_path.mkdir(parents=True, exist_ok=True)
    logger.debug(f"Creating a mongod process at {db_path}")
    subprocess.Popen(["mongod", "--dbpath", db_path], stdout=subprocess.DEVNULL)
    logger.debug(f"Created a mongod process at {db_path}")


@dataclass
class MongodProcess:
    pid: str  # Numeric but still string
    fresh: bool

    def kill(self):
        subprocess.run(["kill", self.pid])

    def clean_up(self):
        if self.fresh:
            self.kill()


def get_mongod_process() -> MongodProcess:
    """Create new ``mongod`` process if one is not found. Either way, return the pid of the
    running process. Also return a bool to indicate whether this was created afresh,
    so that the caller can decide whether to kill the process when finished.
    """
    proc = subprocess.run(["pgrep", "mongod"], capture_output=True)
    nonexisting = proc.returncode != 0
    if nonexisting:
        start_mongod()
        proc = subprocess.run(["pgrep", "mongod"], capture_output=True)
        # If we still couldn't create a mongod process, give up?
        proc.check_returncode()
    pid = proc.stdout.decode().splitlines()[0]
    return MongodProcess(pid=pid, fresh=nonexisting)


# Idea via https://stackoverflow.com/a/60367619/
class MongodExceptionGuard(AbstractContextManager):
    def __init__(self, mongod_proc=get_mongod_process()):
        """Set up the Mongod daemon if a process is not found."""
        self.mongod_proc = mongod_proc

    def __exit__(self, exc_type, exc_value, traceback):
        """If the Mongod daemon was started 'fresh' upon initialisation, kill the process
        upon exitting the context manager (before raising any errors if present).
        """
        if exc_type:
            logger.error(f"{exc_type}, {exc_value}, {traceback}")
            self.mongod_proc.clean_up()
            raise
        else:
            self.mongod_proc.clean_up()
