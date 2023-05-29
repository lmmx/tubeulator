import json
from dataclasses import dataclass, field
from pathlib import Path
from dataclass_wizard import JSONWizard, LoadMeta
from dataclass_wizard.loaders import fromdict
import jsonschema


@dataclass
class ActiveServiceTypeArrayDeserialiser(JSONWizard):
    """
    Autogenerated from Mode::Tfl-Api-Presentation-Entities-ActiveServiceTypeArray
    """

    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(ActiveServiceTypeArrayDeserialiser)


@dataclass
class ActiveServiceTypeDeserialiser(JSONWizard):
    """
    Autogenerated from Mode::Tfl.Api.Presentation.Entities.ActiveServiceType
    """

    Mode: str = None
    ServiceType: str = None

    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(ActiveServiceTypeDeserialiser)


@dataclass
class PredictionArrayDeserialiser(JSONWizard):
    """
    Autogenerated from Mode::Tfl-Api-Presentation-Entities-PredictionArray-4
    """

    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(PredictionArrayDeserialiser)


@dataclass
class PredictionDeserialiser(JSONWizard):
    """
    Autogenerated from Mode::Tfl.Api.Presentation.Entities.Prediction
    """

    Id: str = None
    OperationType: int = None
    VehicleId: str = None
    NaptanId: str = None
    StationName: str = None
    LineId: str = None
    LineName: str = None
    PlatformName: str = None
    Direction: str = None
    Bearing: str = None
    DestinationNaptanId: str = None
    DestinationName: str = None
    Timestamp: str = None
    TimeToStation: int = None
    CurrentLocation: str = None
    Towards: str = None
    ExpectedArrival: str = None
    TimeToLive: str = None
    ModeName: str = None
    Timing: dict = None

    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(PredictionDeserialiser)


@dataclass
class PredictionTimingDeserialiser(JSONWizard):
    """
    Autogenerated from Mode::Tfl.Api.Presentation.Entities.PredictionTiming
    """

    CountdownServerAdjustment: str = None
    Source: str = None
    Insert: str = None
    Read: str = None
    Sent: str = None
    Received: str = None

    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(PredictionTimingDeserialiser)
