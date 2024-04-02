from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path

from .. import __path__

__all__ = [
    "pkg_path",
    "data_path",
    "db_path",
    "openapi_schemas_path",
    "openapi_unified_path",
    "stationdata_path",
    "stationdata_gtfs_path",
    "stationdata_detailed_path",
    "RefPath",
    "SchemaPath",
    "to_enum_friendly_str",
    "from_enum_friendly_str",
    "DtoEnum",
]

pkg_path = Path(*__path__)
data_path = pkg_path / "data"
db_path = data_path / "db"
openapi_schemas_path = data_path / "openapi"
openapi_unified_path = data_path / "openapi_unified"
stationdata_path = data_path / "stationdata"
stationdata_gtfs_path = stationdata_path / "gtfs"
stationdata_detailed_path = stationdata_path / "detailed"


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
