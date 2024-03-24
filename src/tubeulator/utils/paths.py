import json
from dataclasses import dataclass, field
from enum import Enum
from functools import cache
from pathlib import Path

from .. import __path__

__all__ = [
    "pkg_path",
    "db_path",
    "openapi_schemas_path",
    "openapi_unified_path",
    "find_schema",
    "find_schema_by_name",
    "load_endpoint_schema",
    "load_endpoint_component_schemas",
    "RefPath",
    "SchemaPath",
    "DtoEnum",
    "unified_api_schema",
]

pkg_path = Path(*__path__)
data_path = pkg_path / "data"
db_path = data_path / "db"
openapi_schemas_path = data_path / "openapi"
openapi_unified_path = data_path / "openapi_unified"


def find_schema(schema_dir: Path, match: str = "*", levels: int = 0) -> Path:
    """Get the next schema after traversing the given number of levels (default: no levels,
    i.e. directly in the given directory). The schema must have a ``.json`` suffix.
    """
    try:
        glob_prefix = "*/" * levels
        glob_pattern = f"{glob_prefix}{match}.json"
        return next(schema_dir.glob(glob_pattern))
    except StopIteration:
        raise ValueError(f"No JSON file {levels=} below {schema_dir}")


@cache
def find_schema_by_name(schema_name: str) -> Path:
    return find_schema(schema_dir=openapi_schemas_path, match=schema_name, levels=1)


@cache
def load_endpoint_schema(schema_name: str):
    """Load an entire JSON schema for an API endpoint by its name, e.g. "Line" or "Mode"."""
    endpoint_schema = json.loads(Path(find_schema_by_name(schema_name)).read_text())
    return endpoint_schema


@cache
def load_endpoint_component_schemas(schema_name: str) -> dict[str, dict]:
    """Load all component schemas of a JSON schema for an API endpoint by endpoint name."""
    endpoint_schema = load_endpoint_schema(schema_name)
    component_schemas = endpoint_schema["components"].get("schemas", {})
    return component_schemas


@dataclass
class RefPath:
    path: str = field(repr=False)
    name: str = field(init=False)

    def __post_init__(self):
        self.name = Path(self.path).name


@dataclass
class SchemaPath:
    source: dict[str, str] = field(repr=False)
    ref: RefPath = field(init=False)

    def __post_init__(self):
        ref = self.source.get("items", {}).get("$ref")
        self.ref = RefPath(ref)


def to_enum_friendly_str(name: str) -> str:
    return name.replace("-", "_").replace(".", "__")


def from_enum_friendly_str(name: str) -> str:
    return name.replace("_", "-").replace("__", ".")


class DtoEnum(Enum):
    @classmethod
    def select_component(cls, component_name: str):
        return cls[to_enum_friendly_str(component_name)]


unified_api_schema = find_schema(schema_dir=openapi_unified_path, levels=1)
