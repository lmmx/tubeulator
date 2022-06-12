from __future__ import annotations

from dataclasses import dataclass, field

from dataclass_wizard import JSONWizard

from .request import handle_request

__all__ = ["line_data"]


@dataclass
class Line_StopPointsByPathId(JSONWizard):
    values_go_here: str  # TODO


def line_data(creds: dict[str, str]):
    endpoint = "http://api.tfl.gov.uk/Line/"
    url = endpoint + "..."
    response = handle_request(url, creds)
