from __future__ import annotations

from enum import Enum

import patito as pt
from patito import Model
from pydantic import PrivateAttr

__all__ = [
    "StationPoint",
    "Station",
    "Platform",
    "PlatformService",
    "ModeAndLine",
    "CardinalDirectionEnum",
]


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


class Station(Model):
    _source: str = PrivateAttr("Stations.csv")
    StationUniqueId: str = pt.Field(derived_from="UniqueId")
    StationName: str = pt.Field(derived_from="Name")
    FareZones: str  # |-separated list[str]
    HubNaptanCode: str | None
    Wifi: bool
    OutsideStationUniqueId: str
    # Other fields not included here...


class Platform(Model):
    _source: str = PrivateAttr("Platforms.csv")
    PlatformUniqueId: str = pt.Field(derived_from="UniqueId")
    StationUniqueId: str
    PlatformNumber: str | None
    CardinalDirection: str | None  # CardinalDirectionEnum
    PlatformNaptanCode: str | None
    PlatformFriendlyName: str = pt.Field(derived_from="FriendlyName")
    IsCustomerFacing: bool
    HasServiceInterchange: bool
    # Other fields not included here...


class PlatformService(Model):
    _source: str = PrivateAttr("PlatformServices.csv")
    PlatformUniqueId: str
    StopAreaNaptanCode: str
    Line: str  # corresponds to Name in the ModesAndLines model
    DirectionTowards: str | None
    # Other fields not included here...
    PlatformServiceGroupName: str | None = pt.Field(derived_from="GroupName")


class ModeAndLine(Model):
    _source: str = PrivateAttr("ModesAndLines.csv")
    Mode: str
    Name: str


class CardinalDirectionEnum(Enum):
    Westbound = "WB"
    Eastbound = "EB"
    Northbound = "NB"
    Southbound = "SB"
