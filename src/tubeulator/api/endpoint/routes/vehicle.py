"""Accessed via dynamic method resolution under `tubeulator.fetch.vehicle`.

!!! example "Example: `tubeulator.fetch.vehicle.vehicle_arrivals()`"

    ```py
    >>> arrivals = fetch.vehicle.vehicle_arrivals(ids="100")
    >>> len(arrivals)
    9
    >>> print(arrivals[0].model_dump_json(indent=2))
    {
      "Id": "1163507335",
      "OperationType": 1,
      "VehicleId": "100",
      "NaptanId": "940GZZLUHGT",
      "StationName": "Highgate Underground Station",
      "LineId": "northern",
      "LineName": "Northern",
      "PlatformName": "Northbound - Platform 1",
      "Direction": "outbound",
      "Bearing": "",
      "DestinationNaptanId": "940GZZLUHBT",
      "DestinationName": "High Barnet Underground Station",
      "Timestamp": "2024-05-21T23:20:28.040799Z",
      "TimeToStation": 32,
      "CurrentLocation": "Between Archway and Highgate",
      "Towards": "High Barnet via Bank",
      "ExpectedArrival": "2024-05-21T23:21:00Z",
      "TimeToLive": "2024-05-21T23:21:00Z",
      "ModeName": "tube",
      "Timing": {
        "CountdownServerAdjustment": "00:00:00",
        "Source": "0001-01-01T00:00:00",
        "Insert": "0001-01-01T00:00:00",
        "Read": "2024-05-21T23:20:03.635000Z",
        "Sent": "2024-05-21T23:20:28Z",
        "Received": "0001-01-01T00:00:00"
      }
    }
    ```
"""

from .types import RouteEnum


class VehicleEndpointRoutes(RouteEnum):
    emission_surcharge = "/EmissionSurcharge"
    """Gets the Emissions Surcharge compliance for the Vehicle"""
    ulez_compliance = "/UlezCompliance"
    """Gets the Ulez Surcharge compliance for the Vehicle"""
    vehicle_arrivals = "/{ids}/Arrivals"
    """Gets the predictions for a given list of vehicle Id's."""
