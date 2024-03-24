import tubeulator
from pytest import mark


@mark.skiponci
def test_first_mode_is_bus():
    modes = tubeulator.fetch.line.meta_modes()
    first_mode_name = modes[0].ModeName
    assert first_mode_name == "bus"
