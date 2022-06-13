from __future__ import annotations

from pprint import pprint

from .._types import ApiAliasToUnifiedEntities
from ..reference import Reference
from .base import ApiSchema
from .unified import single_unified_api_schema

__all__ = ["AliasedApiSchema"]


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
        self.asc_property_refs = {
            entity_alias: [] for entity_alias in self.entity_schemas  # (i.e. its keys)
        }
        """
        ``asc_property_refs`` will store the API schema components' property references
        alongside the entity alias they come from.
        """
        self.resolved_asc_property_refs = {
            entity_alias: [] for entity_alias in self.entity_schemas  # (i.e. its keys)
        }
        """
        ``resolved_asc_property_refs`` will store the 'resolved' or 'dealiased' API
        schema components' property references alongside the entity alias they come from
        """
        for entity_alias, schema_component in self.entity_schemas.items():
            if asc_properties := schema_component.get("properties"):
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
                            is_array=(is_nested_ref := isinstance(v, dict)),
                            entity=v["$ref"] if is_nested_ref else v,
                        )
                        for k, v in asc_prop_type_info.items()
                        if k in ["$ref", "items"]
                    )
                    for asc_prop, asc_prop_type_info in asc_properties.items()
                    if (
                        "$ref" in asc_prop_type_info
                        or "$ref" in asc_prop_type_info.get("items", {})
                    )
                ]
                assert self.asc_property_refs[entity_alias] == [], "Expected fresh list"
                self.asc_property_refs[entity_alias].extend(asc_property_refs)
                self.pprint_asc_property_refs(alias=entity_alias)
                self.resolve_asc_property_refs(alias=entity_alias)

    @property
    def any_referential_properties(self) -> bool:
        """
        If any of the API schema component properties included a reference to another
        entity, then the values of the ``asc_property_refs`` attribute dictionary will
        be non-empty.
        """
        return any(v for v in self.asc_property_refs.values())

    def pprint_asc_property_refs(self, alias: str) -> None:
        if asc_property_refs := self.asc_property_refs[alias]:
            pprint(asc_property_refs)
            completability = [
                asc_property_ref.is_completable(api_inventory=self.alias2ents)
                for asc_property_ref in asc_property_refs
            ]
            print(
                f"Completable: {completability.count(True)}, incomplete: {completability.count(False)}"
            )

    def resolve_asc_property_refs(self, alias: str) -> int:
        """
        Resolve any 'completable' references, and return the number that were resolved,
        making it possible to ``while`` loop over this method to resolve all references.
        """
        resolved_property_refs = []
        if asc_property_refs := self.asc_property_refs[alias]:
            for asc_property_ref in asc_property_refs:
                if asc_property_ref.is_completable(api_inventory=self.alias2ents):
                    completed = self.dealias_property_reference(ref=asc_property_ref)
                    resolved_property_refs.append(completed)
            print(f"Resolved property refs: {len(resolved_property_refs)}")
            self.resolved_asc_property_refs[alias].extend(resolved_property_refs)
        breakpoint()
        return len(resolved_property_refs)

    def pprint_api_inventory(self) -> None:
        """
        Print the API inventory and a newline if any referential properties printed.
        """
        if self.any_referential_properties:
            pprint({k: v for k, v in self.alias2ents.items() if "Response" not in k})
            print()
            # breakpoint()

    def dealias_property_reference(self, ref: Reference) -> Reference:
        """
        Substitute the aliased entity, which has the format
        ``"#/components/schemas/{ref.alias}"``, with the proper entity name from the
        unified API, which must be 'completable' i.e. exist in the ``self.alias2ents``
        dictionary.

        The new :obj:`Reference` will then suffice to modify the API schema property
        dictionary so as to make it identical to one in the unified API, and thereby
        facilitate matching, and thus resolving the alias to its proper name.
        """
        # Take the first item in the list: no way to distinguish b/w multiple options
        # (if this doesn't work then consider iterating over possible multiple options)
        dealiased_ref_entity = self.alias2ents[ref.substituted_ref][0]
        new_entity = ref.entity[: -len(ref.substituted_ref)] + dealiased_ref_entity
        dealiased_ref = Reference(
            schema=ref.schema,
            alias=ref.alias,
            referential_property=ref.referential_property,
            is_array=ref.is_array,
            entity=new_entity,
        )
        return dealiased_ref
