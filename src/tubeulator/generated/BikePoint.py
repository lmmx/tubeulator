import json
from dataclasses import dataclass, field
from pathlib import Path
from dataclass_wizard import JSONWizard, LoadMeta
from dataclass_wizard.loaders import fromdict
import jsonschema


@dataclass
class PlaceArrayDeserialiser(JSONWizard):
    """
    Autogenerated from BikePoint::Tfl-Api-Presentation-Entities-PlaceArray
    """

    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(PlaceArrayDeserialiser)


@dataclass
class PlaceDeserialiser(JSONWizard):
    """
    Autogenerated from BikePoint::Tfl.Api.Presentation.Entities.Place
    """

    Id: str = None
    Url: str = None
    CommonName: str = None
    Distance: Any = None
    PlaceType: str = None
    AdditionalProperties: list[dict] = field(default_factory=list)
    Children: list[dict] = field(default_factory=list)
    ChildrenUrls: list[str] = field(default_factory=list)
    Lat: Any = None
    Lon: Any = None

    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(PlaceDeserialiser)


@dataclass
class AdditionalPropertiesDeserialiser(JSONWizard):
    """
    Autogenerated from BikePoint::Tfl.Api.Presentation.Entities.AdditionalProperties
    """

    Category: str = None
    Key: str = None
    SourceSystemKey: str = None
    Value: str = None
    Modified: str = None

    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(AdditionalPropertiesDeserialiser)
