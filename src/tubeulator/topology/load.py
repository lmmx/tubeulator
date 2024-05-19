from typing import TypeVar

import patito as pt

from ..utils.paths import stationdata_detailed_path
from .data_model import (
    ModeAndLine,
    Platform,
    PlatformService,
    Station,
    StationPoint,
)

__all__ = [
    "load_model",
    "load_lines",
    "load_platforms",
    "load_platform_services",
    "load_stations",
    "load_station_points",
]

M = TypeVar("M", bound=pt.Model)


def load_model(model_class: M) -> pt.DataFrame:
    """Load the CSV file associated with a patito model `model_class`."""
    source_csv = stationdata_detailed_path / model_class._source.default
    dataset = model_class.DataFrame.read_csv(source_csv)
    dataset = dataset[model_class.columns]
    dataset.validate()
    return dataset


def load_lines() -> pt.DataFrame:
    return load_model(ModeAndLine)


def load_platforms() -> pt.DataFrame:
    return load_model(Platform)


def load_platform_services() -> pt.DataFrame:
    return load_model(PlatformService)


def load_stations() -> pt.DataFrame:
    return load_model(Station)


def load_station_points() -> pt.DataFrame:
    return load_model(StationPoint)
