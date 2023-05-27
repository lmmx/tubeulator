import json
from dataclasses import dataclass, field
from pathlib import Path
from dataclass_wizard import JSONWizard, LoadMeta
from dataclass_wizard.loaders import fromdict
import jsonschema

@dataclass
class UnknownResponseDeserialiser(JSONWizard):
    """
    Autogenerated from Disruptions-Lifts-v2::Unknown
    """
    icsCode: str = None
    naptanCode: str = None
    stopPointName: str = None
    outageStartArea: str = None
    outageEndArea: str = None
    message: str = None
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(UnknownResponseDeserialiser)