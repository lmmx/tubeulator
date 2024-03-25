import tubeulator


def test_identifier_parse():
    """This was a problem case due to the key and the model class name matching."""
    dto = tubeulator.generated.Journey.Identifier
    data = {"crowding": {"passengerFlows": [], "trainLoadings": []}}
    dto.model_validate(data)
