"""Accessed via dynamic method resolution under `tubeulator.fetch.accident_stats`.

!!! example "Example: `tubeulator.fetch.accident_stats.year_accidents()`"

    ```py
    >>> accidents = fetch.accident_stats.year_accidents(year=2019)
    >>> print(accidents[0].model_dump_json(indent=2))
    {
      "Id": 345979,
      "Lat": 51.570865,
      "Lon": -0.231959,
      "Location": "On Edgware Road Near The Junction With north Circular Road",
      "Date": "2019-01-04T21:22:00Z",
      "Severity": "Slight",
      "Borough": "Barnet",
      "Casualties": [
        {
          "Age": 20,
          "Class": "Driver",
          "Severity": "Slight",
          "Mode": "PoweredTwoWheeler",
          "AgeBand": "Adult"
        }
      ],
      "Vehicles": [
        {
          "Type": "Motorcycle_500cc_Plus"
        },
        {
          "Type": "Car"
        }
      ]
    }
    ```
"""

from .types import RouteEnum


class AccidentStatsEndpointRoutes(RouteEnum):
    year_accidents = "/{year}"
    """Gets all accident details for accidents occuring in the specified year"""
