from pathlib import Path

from .. import __path__

__all__ = [
    "pkg_path",
    "db_path",
    "openapi_schemas_path",
    "openapi_unified_path",
    "find_schema",
    "find_schema_by_name",
    "unified_api_schema",
]

pkg_path = Path(*__path__)
data_path = pkg_path / "data"
db_path = data_path / "db"
openapi_schemas_path = data_path / "openapi"
openapi_unified_path = data_path / "openapi_unified"


def find_schema(schema_dir: Path, match: str = "*", levels: int = 0) -> Path:
    """
    Get the next schema after traversing the given number of levels (default: no levels,
    i.e. directly in the given directory). The schema must have a ``.json`` suffix.
    """
    try:
        glob_prefix = "*/" * levels
        glob_pattern = f"{glob_prefix}{match}.json"
        return next(schema_dir.glob(glob_pattern))
    except StopIteration:
        raise ValueError(f"No JSON file {levels=} below {schema_dir}")


def find_schema_by_name(schema_name: str) -> Path:
    return find_schema(schema_dir=openapi_schemas_path, match=schema_name, levels=1)


unified_api_schema = find_schema(schema_dir=openapi_unified_path, levels=1)
