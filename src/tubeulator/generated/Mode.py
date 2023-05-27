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
    mode: str = None
    serviceType: str = None
    
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
    id: str = None
    operationType: int = None
    vehicleId: str = None
    naptanId: str = None
    stationName: str = None
    lineId: str = None
    lineName: str = None
    platformName: str = None
    direction: str = None
    bearing: str = None
    destinationNaptanId: str = None
    destinationName: str = None
    timestamp: str = None
    timeToStation: int = None
    currentLocation: str = None
    towards: str = None
    expectedArrival: str = None
    timeToLive: str = None
    modeName: str = None
    timing: dict = None
    
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
    countdownServerAdjustment: str = None
    source: str = None
    insert: str = None
    read: str = None
    sent: str = None
    received: str = None
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(PredictionTimingDeserialiser)
