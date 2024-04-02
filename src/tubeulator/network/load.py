from pathlib import Path

import patito as pt

from tubeulator.utils.paths import stationdata_gtfs_path

from .data_model import Stop

__all__ = ["load_transport_network"]


def load_transport_network(
    source: Path = stationdata_gtfs_path / "stops.txt",
) -> pt.DataFrame:
    stops = Stop.DataFrame.read_csv(source)
    return stops
