from .types import RouteEnum


class OccupancyEndpointRoutes(RouteEnum):
    BIKE_POINTS = "/BikePoints/{ids}"
    """Get the occupancy for bike points."""
    CAR_PARK = "/CarPark"
    """Gets the occupancy for all car parks that have occupancy data"""
    CAR_PARK_ID = "/CarPark/{id}"
    """Gets the occupancy for a car park with a given id"""
    CHARGE_CONNECTOR = "/ChargeConnector"
    """Gets the occupancy for all charge connectors"""
    CHARGE_CONNECTOR_IDS = "/ChargeConnector/{ids}"
    """Gets the occupancy for a charge connectors with a given id (sourceSystemPlaceId)"""
