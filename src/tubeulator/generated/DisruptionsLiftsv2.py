import json
from typing import Any
from dataclasses import dataclass, field
from pathlib import Path
from dataclass_wizard import JSONWizard
from dataclass_wizard.loaders import fromdict
import jsonschema
from ..utils.paths import load_endpoint_component_schemas

@dataclass
class LiftDisruptionDeserialiser(JSONWizard):
    """
    Autogenerated from Disruptions-Lifts-v2::LiftDisruption
    """
    IcsCode: str = None
    NaptanCode: str = None
    StopPointName: str = None
    OutageStartArea: str = None
    OutageEndArea: str = None
    Message: str = None
    __source_schema_name: str = 'Disruptions-Lifts-v2'
    __component_schema_name: str = 'LiftDisruption'
    
    @classmethod
    def from_dict(cls, o):
        parent_schema = load_endpoint_component_schemas(cls.__source_schema_name)
        schema = parent_schema[cls.__component_schema_name]
        jsonschema.validate(o, schema)
        return fromdict(cls, o)
    
    class Meta(JSONWizard.Meta):
        key_transform_with_load = "PASCAL"
        raise_on_unknown_json_key = True


@dataclass
class DisruptionsLiftsv2ResponseDeserialiser(JSONWizard):
    """
    Autogenerated from Disruptions-Lifts-v2::LiftDisruption
    """
    __source_schema_name: str = 'Disruptions-Lifts-v2'
    __component_schema_name: str = 'Get200ApplicationJsonResponse'
    
    @classmethod
    def from_dict(cls, o):
        parent_schema = load_endpoint_component_schemas(cls.__source_schema_name)
        schema = parent_schema[cls.__component_schema_name]
        jsonschema.validate(o, schema)
        return fromdict(cls, o)
    
    class Meta(JSONWizard.Meta):
        key_transform_with_load = "PASCAL"
        raise_on_unknown_json_key = True