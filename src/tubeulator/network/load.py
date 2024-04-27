from pathlib import Path

import patito as pt

from tubeulator.utils.paths import stationdata_gtfs_path

from .data_model import Stop

__all__ = ["load_transport_network", "load_stations"]


def load_transport_network(
    source: Path = stationdata_gtfs_path / "stops.txt",
) -> pt.DataFrame:
    stops = Stop.DataFrame.read_csv(source)
    stops.validate()
    return stops


def load_stations() -> pt.DataFrame:
    """Load a DataFrame of ID and name for all stations.

    The stop_id and stop_code are identical for the stations."""
    network = load_transport_network()
    stations = network.filter(pt.col("location_type") == 1)
    station_columns = ["stop_id", "stop_name"]  # stations.columns[:3]
    return stations[station_columns]


def load_stops() -> pt.DataFrame:
    """Load a DataFrame of ID and name for all stops.

    The stop_id and stop_code are not identical for the stops."""
    network = load_transport_network()
    stations = network.filter(pt.col("location_type") != 1)
    return stations
    # station_columns = ["stop_id", "stop_name"]  # stations.columns[:3]
    # return stations[station_columns]
