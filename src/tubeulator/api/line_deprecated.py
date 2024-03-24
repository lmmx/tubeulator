"""Functions for the Line API endpoints
"""
from __future__ import annotations

from dataclasses import dataclass

from dataclass_wizard import JSONWizard

from .request import tfl_request

__all__ = ["line_data"]


@dataclass
class Line_StopPointsByPathId(JSONWizard):
    values_go_here: str  # TODO


def line_data(creds: dict[str, str]):
    modes_ep = "Line/Meta/Modes"
    response = tfl_request(endpoint=modes_ep, credentials=creds)
    return response
