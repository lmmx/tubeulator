from __future__ import annotations

from ._types import ApiInventory, NamespaceInventory
from ..utils.paths import openapi_schemas_path, unified_api_schema, find_schema

import ujson
from pathlib import Path
from pprint import pprint

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
    api_entity_schemas = api_schema_obj["components"].get("schemas", {})
    # Drop any of the entities with 'Array' in, they're not useful
    api_entity_schemas = {
        name: schema
        for name, schema in api_entity_schemas.items()
        if "Array" not in name
    }
    unified_api_schema_obj = ujson.loads(unified_api_schema.read_text())
    unified_api_entity_schemas = unified_api_schema_obj["components"]["schemas"]
    alias2entity: ApiInventory = {
        api_entity: []
        for api_entity in api_entity_schemas
    }
    # First pass, get the exact matches
    for api_entity, api_schema_component in api_entity_schemas.items():
        # if api_schema.stem == "occupancy" and api_entity == "Tfl-2":
        #     breakpoint()
        for unified_entity, unified_schema in unified_api_entity_schemas.items():
            if api_schema_component == unified_schema:
                alias2entity[api_entity].append(unified_entity)
    # TODO: second pass, with substitution of known values
    # TODO: make a class to help identify which aliases are in each schema,
    #       which would then be easier to indicate those 'completable' by substitutions
    # Second pass, resolve the referential matches
    any_referential_properties = False
    for api_entity, api_schema_component in api_entity_schemas.items():
        if (asc_properties := api_schema_component.get("properties")):
            referential_properties = {
                asc_property: {
                    k: v
                    for k,v in asc_property_type_info.items()
                    if k in ["$ref", "items"]
                }
                for asc_property, asc_property_type_info in asc_properties.items()
                if (
                    "$ref" in asc_property_type_info
                    or "$ref" in asc_property_type_info.get("items", {})
                )
            }
            if referential_properties:
                print(f"{api_schema.stem}: {api_entity}")
                pprint(referential_properties)
                any_referential_properties = True # toggle flag for follow-up
    # Print the API inventory and a newline if any referential properties printed
    if any_referential_properties:
        pprint({k: v for k,v in alias2entity.items() if "Response" not in k})
        print()
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
