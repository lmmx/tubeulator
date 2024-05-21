"""Accessed via dynamic method resolution under `tubeulator.fetch.bike_point`.

!!! example "Example: `tubeulator.fetch.bike_point.all_locations()`"

    ```py
    >>> bike_points = fetch.bike_point.all_locations()
    >>> print(bike_points[0].model_dump_json(indent=2))
    {
      "Id": "BikePoints_1",
      "Url": "/Place/BikePoints_1",
      "CommonName": "River Street , Clerkenwell",
      "Distance": null,
      "PlaceType": "BikePoint",
      "AdditionalProperties": [
        {
          "Category": "Description",
          "Key": "TerminalName",
          "SourceSystemKey": "BikePoints",
          "Value": "001023",
          "Modified": "2024-05-21T19:57:48.923000Z"
        },
        {
          "Category": "Description",
          "Key": "Installed",
          "SourceSystemKey": "BikePoints",
          "Value": "true",
          "Modified": "2024-05-21T19:57:48.923000Z"
        },
        {
          "Category": "Description",
          "Key": "Locked",
          "SourceSystemKey": "BikePoints",
          "Value": "false",
          "Modified": "2024-05-21T19:57:48.923000Z"
        },
        {
          "Category": "Description",
          "Key": "InstallDate",
          "SourceSystemKey": "BikePoints",
          "Value": "1278947280000",
          "Modified": "2024-05-21T19:57:48.923000Z"
        },
        {
          "Category": "Description",
          "Key": "RemovalDate",
          "SourceSystemKey": "BikePoints",
          "Value": "",
          "Modified": "2024-05-21T19:57:48.923000Z"
        },
        {
          "Category": "Description",
          "Key": "Temporary",
          "SourceSystemKey": "BikePoints",
          "Value": "false",
          "Modified": "2024-05-21T19:57:48.923000Z"
        },
        {
          "Category": "Description",
          "Key": "NbBikes",
          "SourceSystemKey": "BikePoints",
          "Value": "13",
          "Modified": "2024-05-21T19:57:48.923000Z"
        },
        {
          "Category": "Description",
          "Key": "NbEmptyDocks",
          "SourceSystemKey": "BikePoints",
          "Value": "5",
          "Modified": "2024-05-21T19:57:48.923000Z"
        },
        {
          "Category": "Description",
          "Key": "NbDocks",
          "SourceSystemKey": "BikePoints",
          "Value": "19",
          "Modified": "2024-05-21T19:57:48.923000Z"
        },
        {
          "Category": "Description",
          "Key": "NbStandardBikes",
          "SourceSystemKey": "BikePoints",
          "Value": "13",
          "Modified": "2024-05-21T19:57:48.923000Z"
        },
        {
          "Category": "Description",
          "Key": "NbEBikes",
          "SourceSystemKey": "BikePoints",
          "Value": "0",
          "Modified": "2024-05-21T19:57:48.923000Z"
        }
      ],
      "Children": [],
      "ChildrenUrls": [],
      "Lat": 51.529163,
      "Lon": -0.10997
    }
    ```
"""

from .types import RouteEnum


class BikePointEndpointRoutes(RouteEnum):
    all_locations = "/"
    """Gets all bike point locations. The Place object has an addtionalProperties array
    which contains the nbBikes, nbDocks and nbSpaces numbers which give the status of
    the BikePoint. A mismatch in these numbers i.e. nbDocks - (nbBikes + nbSpaces) != 0
    indicates broken docks."""
    search_stations = "/Search"
    """Search for bike stations by their name, a bike point's name often contains
    information about the name of the street or nearby landmarks, for example. Note that the
    search result does not contain the PlaceProperties i.e. the status or occupancy of the
    BikePoint, to get that information you should retrieve the BikePoint by its id on
    '/BikePoint/id."""
    bike_point_by_id = "/{id}"
    """Gets the bike point with the given id."""
