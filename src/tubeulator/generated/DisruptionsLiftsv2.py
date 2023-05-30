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
class LiftDisruption(JSONWizard):
    """
    Autogenerated from Disruptions-Lifts-v2::LiftDisruption
    """
    IcsCode: str = None
    NaptanCode: str = None
    StopPointName: str = None
    OutageStartArea: str = None
    OutageEndArea: str = None
    Message: str = None
    _source_schema_name: str = field(default='Disruptions-Lifts-v2', repr=False)
    _component_schema_name: str = field(default='LiftDisruption', repr=False)
    
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
class Get200ApplicationJsonResponse(JSONWizard):
    """
    Autogenerated from Disruptions-Lifts-v2::Get200ApplicationJsonResponse
    """
    _source_schema_name: str = field(default='Disruptions-Lifts-v2', repr=False)
    _component_schema_name: str = field(default='Get200ApplicationJsonResponse', repr=False)
    
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
    LiftDisruption = LiftDisruption
    Get200ApplicationJsonResponse = Get200ApplicationJsonResponse