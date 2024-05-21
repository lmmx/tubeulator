"""Accessed via dynamic method resolution under `tubeulator.fetch.vehicle`."""
from .types import RouteEnum


class VehicleEndpointRoutes(RouteEnum):
    emission_surcharge = "/EmissionSurcharge"
    """Gets the Emissions Surcharge compliance for the Vehicle"""
    ulez_compliance = "/UlezCompliance"
    """Gets the Ulez Surcharge compliance for the Vehicle"""
    vehicle_arrivals = "/{ids}/Arrivals"
    """Gets the predictions for a given list of vehicle Id's."""
