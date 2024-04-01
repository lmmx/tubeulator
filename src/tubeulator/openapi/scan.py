from __future__ import annotations

from functools import lru_cache
from pathlib import Path

from ..utils.paths import openapi_schemas_path
from ..utils.schemas import find_schema
from ._types import ApiAliasToUnifiedEntities, NamespaceInventory
from .schema.aliased import AliasedApiSchema

__all__ = ["api_schema_inventory", "scan_namespace"]


# TODO: duplication here suggests need for an API schema class (from JSON to entities)
def api_schema_inventory(api_schema: Path) -> ApiAliasToUnifiedEntities:
    """Make a mapping of all aliases (the arbitrarily named entities) to their (properly
    named) unified entity names.
    """
    aliased_api_schema = AliasedApiSchema(path=api_schema, unified=False)
    # aliased_api_schema.pprint_api_inventory()
    return aliased_api_schema.alias2ents


@lru_cache
def scan_namespace(ignore_responses: bool = False) -> NamespaceInventory:
    api_dirs = [d for d in openapi_schemas_path.iterdir() if d.is_dir()]
    api_schemas = [
        find_schema(schema_dir=api_dir, match=api_dir.stem) for api_dir in api_dirs
    ]
    namespace_inventory = {
        api_schema.stem: {
            alias: entity
            for alias, entity in api_schema_inventory(api_schema).items()
            if "Response" not in alias
            # Responses are v degenerate and make the output unreadable
        }
        for api_schema in api_schemas
    }
    return namespace_inventory


def count_namespace(ignore_responses: bool = False) -> NamespaceInventory:
    ns_inventory = scan_namespace(ignore_responses=ignore_responses)
    ns_counts = {
        schema: {
            "pass": len([v for v in ns_inventory[schema].values() if v]),
            "fail": len([v for v in ns_inventory[schema].values() if not v]),
        }
        for schema in ns_inventory
    }
    ns_summaries = {
        schema: f"{ns_counts[schema]['pass']} of {len(ns_inventory[schema])}"
        for schema in ns_inventory
    }
    return ns_summaries
