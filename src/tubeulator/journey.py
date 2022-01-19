from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

#from .tfl_utils import BookMetadata, get_isbn_metadata
from .log_utils import Console
#from .path_utils import data_path

__all__ = ["Journey", "Place", "Destination", "Departure"]

logger = Console(name=__name__).logger

@dataclass
class Journey:
    A: str
    B: str
    via: list[str] = field(default_factory=list)

class Place:
    ...

@dataclass
class Destination(Place):
    ...

@dataclass
class Departure(Place):
    ...
