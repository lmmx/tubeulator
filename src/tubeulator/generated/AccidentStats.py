import json
from dataclasses import dataclass, field
from pathlib import Path
from dataclass_wizard import JSONWizard, LoadMeta
from dataclass_wizard.loaders import fromdict
import jsonschema

@dataclass
class TflApiPresentationEntitiesAccidentStatsAccidentDetailArrayDeserialiser(JSONWizard):
    """
    Autogenerated from AccidentStats::Tfl-Api-Presentation-Entities-AccidentStats-AccidentDetailArray
    """
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(TflApiPresentationEntitiesAccidentStatsAccidentDetailArrayDeserialiser)


@dataclass
class AccidentDetailDeserialiser(JSONWizard):
    """
    Autogenerated from AccidentStats::Tfl.Api.Presentation.Entities.AccidentStats.AccidentDetail
    """
    id: int = None
    lat: Any = None
    lon: Any = None
    location: str = None
    date: str = None
    severity: str = None
    borough: str = None
    casualties: list[dict] = field(default_factory=list)
    vehicles: list[dict] = field(default_factory=list)
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(AccidentDetailDeserialiser)


@dataclass
class CasualtyDeserialiser(JSONWizard):
    """
    Autogenerated from AccidentStats::Tfl.Api.Presentation.Entities.AccidentStats.Casualty
    """
    age: int = None
    class: str = None
    severity: str = None
    mode: str = None
    ageBand: str = None
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(CasualtyDeserialiser)


@dataclass
class VehicleDeserialiser(JSONWizard):
    """
    Autogenerated from AccidentStats::Tfl.Api.Presentation.Entities.AccidentStats.Vehicle
    """
    type: str = None
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(VehicleDeserialiser)


@dataclass
class TflApiPresentationEntitiesAccidentStatsAccidentDetailArray1Deserialiser(JSONWizard):
    """
    Autogenerated from AccidentStats::Tfl-Api-Presentation-Entities-AccidentStats-AccidentDetailArray-1
    """
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(TflApiPresentationEntitiesAccidentStatsAccidentDetailArray1Deserialiser)


@dataclass
class TflApiPresentationEntitiesAccidentStatsAccidentDetailArray2Deserialiser(JSONWizard):
    """
    Autogenerated from AccidentStats::Tfl-Api-Presentation-Entities-AccidentStats-AccidentDetailArray-2
    """
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(TflApiPresentationEntitiesAccidentStatsAccidentDetailArray2Deserialiser)


@dataclass
class TflApiPresentationEntitiesAccidentStatsAccidentDetailArray3Deserialiser(JSONWizard):
    """
    Autogenerated from AccidentStats::Tfl-Api-Presentation-Entities-AccidentStats-AccidentDetailArray-3
    """
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(TflApiPresentationEntitiesAccidentStatsAccidentDetailArray3Deserialiser)