from __future__ import annotations

from ._types import ApiInventory, NamespaceInventory
from ..utils.paths import openapi_schemas_path, unified_api_schema, find_schema

import ujson
from pathlib import Path

__all__ = ["api_schema_inventory", "scan_namespace"]


# TODO: duplication here suggests need for an API schema class (from JSON to entities)
def api_schema_inventory(api_schema: Path) -> ApiInventory:
    """
    Make a mapping of all aliases (the arbitrarily named entities) to their (properly
    named) unified entity names.
    """
    if api_schema.suffix != ".json":
        raise ValueError(f"{api_schema=} is not a JSON file")
    api_schema_obj = ujson.loads(api_schema.read_text())
    api_entity_schemas = api_schema_obj["components"]["schemas"]
    unified_api_schema_obj = ujson.loads(unified_api_schema.read_text())
    unified_api_entity_schemas = unified_api_schema_obj["components"]["schemas"]
    alias2entity: ApiInventory = {
        api_entity: []
        for api_entity in api_entity_schemas
    }
    # First pass, get the exact matches
    for api_entity, api_schema in api_entity_schemas.items():
        for unified_entity, unified_schema in unified_api_entity_schemas.items():
            if api_schema == unified_schema:
                alias2entity[api_entity].append(unified_entity)
    # TODO: second pass, with substitution of known values
    # TODO: make a class to help identify which aliases are in each schema,
    #       which would then be easier to indicate those 'completable' by substitutions
    # {
    #     api_entity: unified_api_entity
    #     for api_entity in api_schema
    # } # ApiInventory
    return alias2entity


def scan_namespace() -> NamespaceInventory:
    api_dirs = [d for d in openapi_schemas_path.iterdir() if d.is_dir()]
    api_schemas = [
        find_schema(schema_dir=api_dir, match=api_dir.stem) for api_dir in api_dirs
    ]
    namespace_inventory = {
        api_schema.stem: api_schema_inventory(api_schema) for api_schema in api_schemas
    }
    # ApiInventory = dict[ApiEntity, UnifiedApiEntity]
    return namespace_inventory
