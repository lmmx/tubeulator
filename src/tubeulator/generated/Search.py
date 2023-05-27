import json
from dataclasses import dataclass, field
from pathlib import Path
from dataclass_wizard import JSONWizard, LoadMeta
from dataclass_wizard.loaders import fromdict
import jsonschema

@dataclass
class SearchMatchDeserialiser(JSONWizard):
    """
    Autogenerated from Search::Tfl.Api.Presentation.Entities.SearchMatch
    """
    id: str = None
    url: str = None
    name: str = None
    lat: Any = None
    lon: Any = None
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(SearchMatchDeserialiser)


@dataclass
class SearchResponseDeserialiser(JSONWizard):
    """
    Autogenerated from Search::Tfl.Api.Presentation.Entities.SearchResponse
    """
    query: str = None
    from: int = None
    page: int = None
    pageSize: int = None
    provider: str = None
    total: int = None
    matches: list[dict] = field(default_factory=list)
    maxScore: Any = None
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(SearchResponseDeserialiser)


@dataclass
class UnknownResponseDeserialiser(JSONWizard):
    """
    Autogenerated from Search::Unknown
    """
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(UnknownResponseDeserialiser)


@dataclass
class UnknownResponseDeserialiser(JSONWizard):
    """
    Autogenerated from Search::Unknown
    """
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(UnknownResponseDeserialiser)


@dataclass
class UnknownResponseDeserialiser(JSONWizard):
    """
    Autogenerated from Search::Unknown
    """
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(UnknownResponseDeserialiser)


@dataclass
class UnknownResponseDeserialiser(JSONWizard):
    """
    Autogenerated from Search::Unknown
    """
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(UnknownResponseDeserialiser)


@dataclass
class UnknownResponseDeserialiser(JSONWizard):
    """
    Autogenerated from Search::Unknown
    """
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(UnknownResponseDeserialiser)


@dataclass
class UnknownResponseDeserialiser(JSONWizard):
    """
    Autogenerated from Search::Unknown
    """
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(UnknownResponseDeserialiser)


@dataclass
class UnknownResponseDeserialiser(JSONWizard):
    """
    Autogenerated from Search::Unknown
    """
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(UnknownResponseDeserialiser)


@dataclass
class UnknownResponseDeserialiser(JSONWizard):
    """
    Autogenerated from Search::Unknown
    """
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(UnknownResponseDeserialiser)


@dataclass
class UnknownResponseDeserialiser(JSONWizard):
    """
    Autogenerated from Search::Unknown
    """
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(UnknownResponseDeserialiser)


@dataclass
class UnknownResponseDeserialiser(JSONWizard):
    """
    Autogenerated from Search::Unknown
    """
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(UnknownResponseDeserialiser)


@dataclass
class UnknownResponseDeserialiser(JSONWizard):
    """
    Autogenerated from Search::Unknown
    """
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(UnknownResponseDeserialiser)


@dataclass
class UnknownResponseDeserialiser(JSONWizard):
    """
    Autogenerated from Search::Unknown
    """
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(UnknownResponseDeserialiser)