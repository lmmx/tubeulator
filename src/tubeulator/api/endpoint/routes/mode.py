"""Accessed via dynamic method resolution under `tubeulator.fetch.mode`.

!!! example "Example: `tubeulator.fetch.mode.mode_arrivals()`"

    ```py
    >>> arrivals = tubeulator.fetch.mode.mode_arrivals(mode="tube")
    >>> print(arrivals[0].model_dump_json(indent=2))
    {
      "Id": "548560311",
      "OperationType": 1,
      "VehicleId": "305",
      "NaptanId": "940GZZLUSWK",
      "StationName": "Southwark Underground Station",
      "LineId": "jubilee",
      "LineName": "Jubilee",
      "PlatformName": "Westbound - Platform 1",
      "Direction": "inbound",
      "Bearing": "",
      "DestinationNaptanId": "940GZZLUSTM",
      "DestinationName": "Stanmore Underground Station",
      "Timestamp": "2024-05-21T22:59:57.338367Z",
      "TimeToStation": 16,
      "CurrentLocation": "Between London Bridge and Southwark",
      "Towards": "Stanmore",
      "ExpectedArrival": "2024-05-21T23:00:13Z",
      "TimeToLive": "2024-05-21T23:00:13Z",
      "ModeName": "tube",
      "Timing": {
        "CountdownServerAdjustment": "00:00:00",
        "Source": "0001-01-01T00:00:00",
        "Insert": "0001-01-01T00:00:00",
        "Read": "2024-05-21T22:59:28.617000Z",
        "Sent": "2024-05-21T22:59:57Z",
        "Received": "0001-01-01T00:00:00"
      }
    }
    ```
"""

from .types import RouteEnum


class ModeEndpointRoutes(RouteEnum):
    active_service_types = "/ActiveServiceTypes"
    """Returns the service type active for a mode. Currently only supports tube"""
    mode_arrivals = "/{mode}/Arrivals"
    """Gets the next arrival predictions for all stops of a given mode"""
