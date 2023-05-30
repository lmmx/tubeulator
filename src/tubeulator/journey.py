from __future__ import annotations

from dataclasses import dataclass, field

from .utils.logs import set_up_logging

__all__ = ["Journey", "Place", "Destination", "Departure"]

logger = set_up_logging(name=__name__)


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
