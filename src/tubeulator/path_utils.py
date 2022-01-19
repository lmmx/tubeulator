from __future__ import annotations

from pathlib import Path

from . import __path__

__all__ = ["pkg_path"]

pkg_path = Path(*__path__)
