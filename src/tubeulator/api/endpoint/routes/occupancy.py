"""Accessed via dynamic method resolution under `tubeulator.fetch.occupancy`."""

from .types import RouteEnum


class OccupancyEndpointRoutes(RouteEnum):
    bike_points = "/BikePoints/{ids}"
    """Get the occupancy for bike points."""
    car_park = "/CarPark"
    """Gets the occupancy for all car parks that have occupancy data"""
    car_park_id = "/CarPark/{id}"
    """Gets the occupancy for a car park with a given id"""
    charge_connector = "/ChargeConnector"
    """Gets the occupancy for all charge connectors"""
    charge_connector_ids = "/ChargeConnector/{ids}"
    """Gets the occupancy for a charge connectors with a given id (sourceSystemPlaceId)"""
