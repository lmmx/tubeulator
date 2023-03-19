from enum import Enum


class VehicleEndpointRoutes(Enum):
    EMISSION_SURCHARGE = "/EmissionSurcharge"
    """Gets the Emissions Surcharge compliance for the Vehicle"""
    ULEZ_COMPLIANCE = "/UlezCompliance"
    """Gets the Ulez Surcharge compliance for the Vehicle"""
    VEHICLE_ARRIVALS = "/{ids}/Arrivals"
    """Gets the predictions for a given list of vehicle Id's."""
