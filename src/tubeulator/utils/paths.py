from pathlib import Path

from .. import __path__

__all__ = [
    "pkg_path",
    "db_path",
    "openapi_schemas_path",
    "openapi_unified_path",
    "find_schema",
    "unified_api_schema",
]

pkg_path = Path(*__path__)
db_path = pkg_path / "data" / "db"
openapi_schemas_path = pkg_path / "openapi"
openapi_unified_path = pkg_path / "openapi_unified"


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


unified_api_schema = find_schema(schema_dir=openapi_unified_path, levels=1)
