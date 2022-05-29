from pathlib import Path

from .. import __path__

__all__ = ["pkg_path"]

pkg_path = Path(*__path__)
db_path = pkg_path / "data" / "db"
