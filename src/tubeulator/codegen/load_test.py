"""Import this module to check if the generated Python DTOs are loadable."""

try:
    from ..generated import (
        AccidentStats,
        AirQuality,
        BikePoint,
        DisruptionsLiftsv2,
        Journey,
        Line,
        Mode,
        Place,
        Road,
        Search,
        StopPoint,
        Vehicle,
        crowding,
        occupancy,
    )
except:
    # The load_test is used for parsing, but can block generation
    # Temporarily use pass here to permit regenerating from broken config
    raise  # pass
