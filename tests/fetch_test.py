import tubeulator


def test_first_mode_is_bus():
    modes = tubeulator.fetch.line.meta_modes()
    first_mode_name = modes[0].ModeName
    assert first_mode_name == "bus"


def test_lines_by_ids():
    """This failed due to a codegen error."""
    lines = tubeulator.fetch.line.lines_by_ids("waterloo-city")
