from tubeulator.network.load import load_transport_network


def test_load_gtfs():
    """This was a problem case due to the alias generator."""
    load_transport_network()
