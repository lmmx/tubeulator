from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from pprint import pprint
from typing import Literal

import ujson

from ..utils.paths import find_schema, openapi_schemas_path
from ..utils.paths import unified_api_schema as unified_api_schema_path
from ._types import ApiAliasToUnifiedEntities, NamespaceInventory

__all__ = ["api_schema_inventory", "scan_namespace"]


@dataclass
class Reference:
    schema: str
    alias: str
    referential_property: str
    # path: tuple[Literal["items","$ref"]]
    is_array: bool
    entity: str

    @property
    def path(self) -> tuple[Literal["items", "$ref"]]:
        return tuple([*(["items"] if self.is_array else []), "$ref"])

    @property
    def substituted_ref(self) -> str:
        return Path(self.entity).name

    def is_completable(self, api_inventory: ApiAliasToUnifiedEntities):
        """
        If the API inventory has a resolved value (or values) for the alias referenced
        in the current referential property's ``$ref`` key, then the reference can be
        resolved immediately (i.e. "completed"). If not, we have to wait for the next
        round of substitutions, or chase references.
        """
        if self.substituted_ref in api_inventory:
            return api_inventory[self.substituted_ref] != []
        else:
            raise ValueError(f"{self.substituted_ref=} not found in {api_inventory=}")


@dataclass
class ApiSchema:
    path: Path
    unified: bool

    def __post_init__(self):
        if self.path.suffix != ".json":
            raise ValueError(f"{self.path=} is not a JSON file")
        self.obj = ujson.loads(self.path.read_text())
        # Discard any of the entities with 'Array' in, they're not useful
        self.entity_schemas = {
            name: schema
            for name, schema in self.obj["components"].get("schemas", {}).items()
            if "Array" not in name
        }

    @property
    def name(self) -> str:
        return self.path.stem


class UnifiedApiSchema(ApiSchema):
    """
    A unified API schema.
    """

    unified: bool = True


single_unified_api_schema = UnifiedApiSchema(path=unified_api_schema_path, unified=True)
"""
A singleton instance to avoid re-reading the unified API schema JSON once per
non-unified API schema instantiation.
"""


class AliasedApiSchema(ApiSchema):
    """
    A non-unified API schema.
    """

    unified: bool = False

    def __post_init__(self):
        super().__post_init__()
        self.unified_schema = single_unified_api_schema
        self.alias2ents: ApiAliasToUnifiedEntities = {
            entity_alias: [] for entity_alias in self.entity_schemas  # (i.e. its keys)
        }
        self.match_entities()
        self.resolve_entity_references()

    def match_entities(self):
        """
        First pass, get the exact matches. Iterate over the aliases (the entity names in
        the API schema "broken out" from the unified schema) and where the schema
        component is an exact match for one in the unified schema, store the entity name
        (or names: there is no guarantee only a single entity will match the alias).
        """
        for entity_alias, schema_component in self.entity_schemas.items():
            for entity, unif_schema in self.unified_schema.entity_schemas.items():
                if schema_component == unif_schema:
                    self.alias2ents[entity_alias].append(entity)

    def resolve_entity_references(self):
        """
        Second pass, resolve the referential matches with substitution of known values.
        Again iterate over the aliases, but now try to find where the schema component
        can be substituted if the reference is 'completable' to consequently make an
        exact match for one of the schema components in the unified schema. As for the
        previous pass, store the entity name or names alongside the alias if successful.
        """
        self.any_referential_properties = False
        for entity_alias, schema_component in self.entity_schemas.items():
            if asc_properties := schema_component.get("properties"):
                referential_properties = {
                    asc_property: {
                        k: v
                        for k, v in asc_property_type_info.items()
                        if k in ["$ref", "items"]
                    }
                    for asc_property, asc_property_type_info in asc_properties.items()
                    if (
                        "$ref" in asc_property_type_info
                        or "$ref" in asc_property_type_info.get("items", {})
                    )
                }
                # Either a top-level $ref or as the items in an array.
                # (Valid) arrays have items with a specified $ref
                asc_property_refs = [
                    # Use next as can rely on only 1 reference per property
                    next(
                        Reference(
                            schema=self.name,
                            alias=entity_alias,
                            referential_property=asc_prop,
                            # path=tuple([*(["items"] if (is_nested_ref := isinstance(v, dict)) else []), "$ref"]),
                            is_array=isinstance(v, dict),
                            entity=v["$ref"]
                            if (is_nested_ref := isinstance(v, dict))
                            else v,
                        )
                        for v in asc_prop_type_info.values()
                    )
                    for asc_prop, asc_prop_type_info in referential_properties.items()
                ]
                if referential_properties:
                    pprint(asc_property_refs)
                    self.any_referential_properties = True  # toggle flag for follow-up
                    completability = [
                        asc_property_ref.is_completable(api_inventory=self.alias2ents)
                        for asc_property_ref in asc_property_refs
                    ]
                    print(
                        f"Completable: {completability.count(True)}, incomplete: {completability.count(False)}"
                    )
        # Print the API inventory and a newline if any referential properties printed
        if self.any_referential_properties:
            pprint({k: v for k, v in self.alias2ents.items() if "Response" not in k})
            print()


# TODO: duplication here suggests need for an API schema class (from JSON to entities)
def api_schema_inventory(api_schema: Path) -> ApiAliasToUnifiedEntities:
    """
    Make a mapping of all aliases (the arbitrarily named entities) to their (properly
    named) unified entity names.
    """
    api_schema = AliasedApiSchema(path=api_schema, unified=False)
    return api_schema.alias2ents


def scan_namespace() -> NamespaceInventory:
    api_dirs = [d for d in openapi_schemas_path.iterdir() if d.is_dir()]
    api_schemas = [
        find_schema(schema_dir=api_dir, match=api_dir.stem) for api_dir in api_dirs
    ]
    namespace_inventory = {
        api_schema.stem: api_schema_inventory(api_schema) for api_schema in api_schemas
    }
    return namespace_inventory
