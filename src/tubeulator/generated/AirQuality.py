import json
from dataclasses import dataclass, field
from pathlib import Path
from dataclass_wizard import JSONWizard
from dataclass_wizard.loaders import fromdict
import jsonschema
from ..utils.paths import load_endpoint_component_schemas, DtoEnum

@dataclass
class Object(JSONWizard):
    """
    Autogenerated from AirQuality::System.Object
    """
    _source_schema_name: str = 'AirQuality'
    _component_schema_name: str = 'System.Object'
    
    @classmethod
    def from_dict(cls, o):
        parent_schema = load_endpoint_component_schemas(cls._source_schema_name)
        schema = parent_schema[cls._component_schema_name]
        jsonschema.validate(o, schema)
        return fromdict(cls, o)
    
    class Meta(JSONWizard.Meta):
        key_transform_with_load = 'PASCAL'


class Deserialisers(DtoEnum):
    System__Object = Object