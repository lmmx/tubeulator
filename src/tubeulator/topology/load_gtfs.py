"""Deprecated methods, GTFS data isn't very useful on its own."""

from pathlib import Path

import patito as pt

from ..utils.paths import stationdata_gtfs_path
from .data_model import GTFSStop

__all__ = ["load_transport_topology", "load_stations"]


def load_transport_topology(
    source: Path = stationdata_gtfs_path / "stops.txt",
) -> pt.DataFrame:
    stops = GTFSStop.DataFrame.read_csv(source)
    stops.validate()
    return stops


def load_stations() -> pt.DataFrame:
    """Load a DataFrame of ID and name for all stations.

    The stop_id and stop_code are identical for the stations."""
    topology = load_transport_topology()
    stations = topology.filter(pt.col("location_type") == 1)
    station_columns = ["stop_id", "stop_name"]  # stations.columns[:3]
    return stations[station_columns]


def load_stops() -> pt.DataFrame:
    """Load a DataFrame of ID and name for all stops.

    The stop_id and stop_code are not identical for the stops."""
    topology = load_transport_topology()
    stations = topology.filter(pt.col("location_type") != 1)
    return stations
    # station_columns = ["stop_id", "stop_name"]  # stations.columns[:3]
    # return stations[station_columns]
