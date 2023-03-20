from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from urllib.parse import urlencode

import httpx

from .endpoint.names import EndpointNames
from .endpoint.routes.types import AnyEndpointRouteEnum

__all__ = ["tfl_request"]


class TflApiPath:
    root: str = "https://api.tfl.gov.uk/"


@dataclass
class Path(TflApiPath):
    endpoint: EndpointNames
    route: AnyEndpointRouteEnum
    vars: list = field(init=False)

    class Var(Enum):
        DAY_OF_WEEK = "DayOfWeek"
        NAPTAN = "Naptan"
        DIRECTION = "direction"
        DISRUPTION_IDS = "disruptionIds"
        END_DATE = "endDate"
        FROM = "from"
        FROM_STOP_POINT_ID = "fromStopPointId"
        ID = "id"
        IDS = "ids"
        LAT = "lat"
        LINE = "line"
        LINE_ID = "lineId"
        LON = "lon"
        MODE = "mode"
        MODES = "modes"
        PAGE = "page"
        QUERY = "query"
        SEVERITY = "severity"
        START_DATE = "startDate"
        STOP_POINT_ID = "stopPointId"
        TO = "to"
        TO_STOP_POINT_ID = "toStopPointId"
        TYPE = "type"
        TYPES = "types"
        YEAR = "year"

    def __post_init__(self):
        self.vars = [
            self.Var(var.strip("{}"))
            for var in self.route.parts
            if var.startswith("{") and var.endswith("}")
        ]

    @property
    def url(self) -> str:
        return f"{self.root}{self.endpoint.value}{self.route.value}"

    @property
    def vars_to_fill(self) -> list[str]:
        return [var.value for var in self.vars]

    def check_vars_supplied(self, *args, **kwargs) -> dict:
        """Basic input validation, not type validation."""
        if args and kwargs:
            self.invalidate(
                "You can't mix args and kwargs, pick one.",
                rcvd={"args": args, "kwargs": kwargs},
            )
        elif self.vars and not (args or kwargs):
            self.invalidate("No vars supplied.", rcvd={"args": args, "kwargs": kwargs})
        if args and len(args) < len(self.path.vars):
            self.invalidate("Missing arguments", rcvd=args)
        elif kwargs and set(self.vars_to_fill) != set(kwargs):
            self.invalidate("Missing parameters", rcvd=kwargs)

    def invalidate(self, reason: str, rcvd: list[str] | dict):
        raise ValueError(f"Bad request ({reason}): {self.vars_to_fill=}, got {rcvd}")

    def build_url(self, *args, **kwargs) -> str:
        self.check_vars_supplied(*args, **kwargs)
        params = dict(zip(self.vars_to_fill, args)) if args else kwargs
        return self.url.format(**params)


@dataclass
class Request:
    path: Path

    def __call__(self, *args, **kwargs):
        return self.send(*args, **kwargs)

    def send(self, *args, **kwargs):
        url = self.path.build_url(*args, **kwargs)
        # TODO: make GET request here
        return {"source": url, "response": {"content": "example"}}


def GET(url: str, credentials: dict[str, str]) -> httpx.Response:
    # TODO: get credentials here if not supplied
    params = urlencode(
        {"app_id": credentials["app_id"], "app_key": credentials["primary_key"]}
    )
    return httpx.get(url, params=params)
