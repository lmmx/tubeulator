from __future__ import annotations

from enum import Enum

from patito import Model
from pydantic import PrivateAttr

__all__ = [
    "ModeAndLine",
    "CardinalDirectionEnum",
    "Platform",
    "PlatformService",
    "Station",
    "StationPoint",
]


class ModeAndLine(Model):
    _source: str = PrivateAttr("ModesAndLines.csv")
    Mode: str
    Name: str


class CardinalDirectionEnum(Enum):
    Westbound = "WB"
    Eastbound = "EB"
    Northbound = "NB"
    Southbound = "SB"


class Platform(Model):
    _source: str = PrivateAttr("Platforms.csv")
    UniqueId: str
    StationUniqueId: str
    PlatformNumber: str | None
    CardinalDirection: str | None  # CardinalDirectionEnum
    PlatformNaptanCode: str | None
    FriendlyName: str
    IsCustomerFacing: bool
    HasServiceInterchange: bool
    # AccessibleEntranceName: str | None
    # HasStepFreeRouteInformation: bool


class PlatformService(Model):
    _source: str = PrivateAttr("PlatformServices.csv")
    PlatformUniqueId: str
    StopAreaNaptanCode: str
    Line: str  # corresponds to Name in the ModesAndLines model
    DirectionTowards: str | None
    # Other fields not included here...
    GroupName: str | None


class Station(Model):
    _source: str = PrivateAttr("Stations.csv")
    UniqueId: str
    Name: str
    FareZones: str  # |-separated list[str]
    HubNaptanCode: str | None
    Wifi: bool
    OutsideStationUniqueId: str
    # Other fields not included here...


class StationPoint(Model):
    _source: str = PrivateAttr("StationPoints.csv")
    UniqueId: str
    StationUniqueId: str  # corresponds to UniqueId in the Station model
    AreaName: str
    AreaId: int
    Level: int
    Lat: float
    Lon: float
    FriendlyName: str
