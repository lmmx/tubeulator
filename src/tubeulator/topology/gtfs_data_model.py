from __future__ import annotations

from enum import Enum

from patito import Model


class LocationTypeEnum(Enum):
    Stop = "0"
    Station = "1"
    # EntranceOrExit = "2"  # Not used
    GenericNode = "3"
    # BoardingArea = "4"  # Not used


class GTFSStop(Model):
    stop_id: str
    stop_code: str | None = None
    stop_name: str
    stop_desc: str | None = None
    stop_lat: float | None = None
    stop_lon: float | None = None
    location_type: int  # LocationTypeEnum
    parent_station: str | None = None
    level_id: str | None = None
    platform_code: str | None = None
