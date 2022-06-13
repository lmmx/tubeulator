from __future__ import annotations

from pathlib import Path

from ..utils.paths import find_schema, openapi_schemas_path
from ._types import ApiAliasToUnifiedEntities, NamespaceInventory
from .schema.aliased import AliasedApiSchema

__all__ = ["api_schema_inventory", "scan_namespace"]


# TODO: duplication here suggests need for an API schema class (from JSON to entities)
def api_schema_inventory(api_schema: Path) -> ApiAliasToUnifiedEntities:
    """
    Make a mapping of all aliases (the arbitrarily named entities) to their (properly
    named) unified entity names.
    """
    aliased_api_schema = AliasedApiSchema(path=api_schema, unified=False)
    aliased_api_schema.pprint_api_inventory()
    return aliased_api_schema.alias2ents


def scan_namespace() -> NamespaceInventory:
    api_dirs = [d for d in openapi_schemas_path.iterdir() if d.is_dir()]
    api_schemas = [
        find_schema(schema_dir=api_dir, match=api_dir.stem) for api_dir in api_dirs
    ]
    namespace_inventory = {
        api_schema.stem: api_schema_inventory(api_schema) for api_schema in api_schemas
    }
    return namespace_inventory
