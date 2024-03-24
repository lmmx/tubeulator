from enum import Enum
from typing import TypeVar

__all__ = ["RouteEnum", "AnyEndpointRouteEnum"]


class RouteEnum(Enum):
    """Base route enum which can have methods set on (but no enum members)."""

    @property
    def parts(self):
        return self.value.split("/")


AnyEndpointRouteEnum = TypeVar("AnyEndpointRouteEnum", bound=RouteEnum)
"""Type indicating a specific endpoint (subclass of RouteEnum)"""
