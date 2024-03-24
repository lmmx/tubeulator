from __future__ import annotations
import json
from datetime import datetime
from dataclasses import dataclass, field
from pathlib import Path
from dataclass_wizard import JSONWizard
from dataclass_wizard.loaders import fromdict
import jsonschema
from ..utils.paths import load_endpoint_component_schemas, DtoEnum

@dataclass
class AccidentStatsAccidentDetailArray(JSONWizard):
    """
    Autogenerated from AccidentStats::Tfl-Api-Presentation-Entities-AccidentStats-AccidentDetailArray
    """
    _source_schema_name: str = field(default='AccidentStats', repr=False)
    _component_schema_name: str = field(default='Tfl-Api-Presentation-Entities-AccidentStats-AccidentDetailArray', repr=False)

    @classmethod
    def from_dict(cls, o):
        parent_schema = load_endpoint_component_schemas(cls._source_schema_name)
        schema = parent_schema[cls._component_schema_name]
        jsonschema.validate(o, schema)
        return fromdict(cls, o)

    class Meta(JSONWizard.Meta):
        key_transform_with_load = 'PASCAL'
        recursive_classes = True


@dataclass
class AccidentDetail(JSONWizard):
    """
    Autogenerated from AccidentStats::Tfl.Api.Presentation.Entities.AccidentStats.AccidentDetail
    """
    Id: int = None
    Lat: float = None
    Lon: float = None
    Location: str = None
    Date: datetime = None
    Severity: str = None
    Borough: str = None
    Casualties: list[Casualty] = field(default_factory=list)
    Vehicles: list[Vehicle] = field(default_factory=list)
    _source_schema_name: str = field(default='AccidentStats', repr=False)
    _component_schema_name: str = field(default='Tfl.Api.Presentation.Entities.AccidentStats.AccidentDetail', repr=False)

    @classmethod
    def from_dict(cls, o):
        parent_schema = load_endpoint_component_schemas(cls._source_schema_name)
        schema = parent_schema[cls._component_schema_name]
        jsonschema.validate(o, schema)
        return fromdict(cls, o)

    class Meta(JSONWizard.Meta):
        key_transform_with_load = 'PASCAL'
        recursive_classes = True


@dataclass
class Casualty(JSONWizard):
    """
    Autogenerated from AccidentStats::Tfl.Api.Presentation.Entities.AccidentStats.Casualty
    """
    Age: int = None
    Class: str = None
    Severity: str = None
    Mode: str = None
    AgeBand: str = None
    _source_schema_name: str = field(default='AccidentStats', repr=False)
    _component_schema_name: str = field(default='Tfl.Api.Presentation.Entities.AccidentStats.Casualty', repr=False)

    @classmethod
    def from_dict(cls, o):
        parent_schema = load_endpoint_component_schemas(cls._source_schema_name)
        schema = parent_schema[cls._component_schema_name]
        jsonschema.validate(o, schema)
        return fromdict(cls, o)

    class Meta(JSONWizard.Meta):
        key_transform_with_load = 'PASCAL'
        recursive_classes = True


@dataclass
class Vehicle(JSONWizard):
    """
    Autogenerated from AccidentStats::Tfl.Api.Presentation.Entities.AccidentStats.Vehicle
    """
    Type: str = None
    _source_schema_name: str = field(default='AccidentStats', repr=False)
    _component_schema_name: str = field(default='Tfl.Api.Presentation.Entities.AccidentStats.Vehicle', repr=False)

    @classmethod
    def from_dict(cls, o):
        parent_schema = load_endpoint_component_schemas(cls._source_schema_name)
        schema = parent_schema[cls._component_schema_name]
        jsonschema.validate(o, schema)
        return fromdict(cls, o)

    class Meta(JSONWizard.Meta):
        key_transform_with_load = 'PASCAL'
        recursive_classes = True


class Deserialisers(DtoEnum):
    Tfl_Api_Presentation_Entities_AccidentStats_AccidentDetailArray = AccidentStatsAccidentDetailArray
    Tfl__Api__Presentation__Entities__AccidentStats__AccidentDetail = AccidentDetail
    Tfl__Api__Presentation__Entities__AccidentStats__Casualty = Casualty
    Tfl__Api__Presentation__Entities__AccidentStats__Vehicle = Vehicle