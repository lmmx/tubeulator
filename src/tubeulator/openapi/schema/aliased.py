from __future__ import annotations

import logging
from copy import deepcopy
from pprint import pprint

from .._types import ApiAliasToUnifiedEntities, ApiEntityAlias
from ..reference import AliasToRefs, Reference, dealias_schema
from .base import ApiSchema
from .unified import single_unified_api_schema

__all__ = ["AliasedApiSchema"]

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class AliasedApiSchema(ApiSchema):
    """A non-unified API schema."""

    unified: bool = False

    def __post_init__(self):
        super().__post_init__()
        self.prepare_inventories()
        self.match_entities()
        # self.pprint_api_inventory(nonreferential_ok=True)
        self.chase_entity_references()
        if not self.is_resolved:
            self.property_match()

    @property
    def is_resolved(self) -> bool:
        """If there is no alias in the schema with empty entity list (i.e. unresolved)."""
        return all(self.alias2ents.values())
        # return all(
        #     {
        #         name: entities
        #         for name, entities in self.alias2ents.items()
        #         if not self.is_skipped_name(name=name)
        #     }.values(),
        # )

    def match_entities(self) -> None:
        """First pass, get the exact matches. Iterate over the aliases (the entity names in
        the API schema "broken out" from the unified schema) and where the schema
        component is an exact match for one in the unified schema, store the entity name
        (or names: there is no guarantee only a single entity will match the alias).
        """
        for entity_alias, schema_component in self.entity_schemas.items():
            resolved_ents = []
            for entity, unif_schema in self.unified_schema.entity_schemas.items():
                if schema_component == unif_schema:
                    resolved_ents.append(entity)
            if self.alias2ents[entity_alias] == [] and entity_alias in resolved_ents:
                # The entities with Array in their name will match any other Array,
                # but it's trivially always just going to be the one with same name
                resolved_ents = [entity_alias]
            for entity in resolved_ents:
                self.resolve_alias(alias=entity_alias, entity=entity)

    def resolve_alias(self, alias: ApiEntityAlias, entity: str) -> None:
        if entity not in (entity_list := self.alias2ents[alias]):
            entity_list.append(entity)

    def match_entities_with_modification(
        self,
        alias: ApiEntityAlias,
        property_refs: list[Reference],
    ) -> None:
        """Second pass, get the exact matches after substituting a reference.  Iterate over
        the aliases (the entity names in the API schema "broken out" from the unified
        schema) and where the schema component is an exact match for one in the unified
        schema, store the entity name (or names: there is no guarantee only a single
        entity will match the alias).
        """
        schema_component = self.entity_schemas[alias]
        # Modify the schema dict by replacing the reference (in a copy not the original)
        mod_schema_component = dealias_schema(
            refs=property_refs,
            component=schema_component,
        )
        for entity, unif_schema in self.unified_schema.entity_schemas.items():
            if mod_schema_component == unif_schema:
                self.resolve_alias(alias=alias, entity=entity)

    def chase_entity_references(self) -> None:
        """Run the entity dealiasing/cross-reference in a loop until no more are resolved."""
        iteration_count = 0
        while any((resolution_counts := self.resolve_entity_references()).values()):
            iteration_count += 1
            if iteration_count > 10:
                raise ValueError("Looped too much, something's up")
            for alias, refs in self.resolved_property_refs.items():
                if refs:
                    self.match_entities_with_modification(
                        alias=alias,
                        property_refs=refs,
                    )
            # Keep the running tally of resolved references for each alias up to date
            for alias in self.resolution_counts:
                self.resolution_counts[alias] += resolution_counts[alias]
        else:
            logger.info(
                f"-----RESOLUTION COMPLETE FOR {self.name}: "
                f" ROUNDS: {iteration_count}, "
                f" REFERENTIAL: {self.any_referential_properties}----------",
            )

    def resolve_entity_references(self) -> dict[ApiEntityAlias, int]:
        """Second pass, resolve the referential matches with substitution of known values.
        Again iterate over the aliases, but now try to find where the schema component
        can be substituted if the reference is 'completable' to consequently make an
        exact match for one of the schema components in the unified schema. As for the
        previous pass, store the entity name or names alongside the alias if successful.
        """
        resolution_counts = dict.fromkeys(self.entity_schemas, 0)
        for entity_alias, schema_component in self.entity_schemas.items():
            if properties := schema_component.get("properties"):
                # assert self.property_refs[entity_alias] == [], "Expected fresh list"
                # IMPORTANT: listcomp is used here so list is fixed at this point
                skip_refs = list(self.property_refs[entity_alias])
                """Skip any properties whose references have been resolved already"""
                # Either a top-level $ref or as the items in an array.
                # (Valid) arrays have items with a specified $ref
                property_refs = [
                    # Use next as can rely on only 1 reference per property
                    next(
                        Reference(
                            schema=self.name,
                            alias=entity_alias,
                            referential_property=prop,
                            is_array=(is_nested_ref := isinstance(v, dict)),
                            entity=v["$ref"] if is_nested_ref else v,
                        )
                        for k, v in prop_type_info.items()
                        if k in ["$ref", "items"]
                    )
                    for prop, prop_type_info in properties.items()
                    if (
                        "$ref" in prop_type_info
                        or "$ref" in prop_type_info.get("items", {})
                    )
                    if prop not in [ref.referential_property for ref in skip_refs]
                ]
                logger.debug(f"[{entity_alias}] Adding {property_refs}")
                self.property_refs[entity_alias].extend(property_refs)
                # self.pprint_property_refs(alias=entity_alias)
                n_resolved = self.resolve_refs(alias=entity_alias, skip=skip_refs)
                resolution_counts[entity_alias] += n_resolved
        return resolution_counts

    def pprint_property_refs(self, alias: str) -> None:
        if property_refs := self.property_refs[alias]:
            pprint(property_refs)
            completability = [
                property_ref.is_completable(api_inventory=self.alias2ents)
                for property_ref in property_refs
            ]
            print(
                f"Completable: {completability.count(True)}, incomplete: {completability.count(False)}",
            )

    def resolve_refs(self, alias: str, skip: list[Reference]) -> int:
        """Resolve any 'completable' references, and return the number that were resolved,
        making it possible to ``while`` loop over this method to resolve all references.
        """
        resolved_property_refs = []
        if property_refs := self.property_refs[alias]:
            for property_ref in property_refs:
                if property_ref in skip:
                    continue
                elif property_ref.is_completable(api_inventory=self.alias2ents):
                    completed = self.dealias_property_reference(ref=property_ref)
                    resolved_property_refs.append(completed)
            logger.debug(f"Resolved property refs: {len(resolved_property_refs)}")
            self.resolved_property_refs[alias].extend(resolved_property_refs)
        return len(resolved_property_refs)

    def pprint_api_inventory(self, nonreferential_ok: bool = False) -> None:
        """Print the API inventory and a newline if any referential properties printed."""
        if self.any_referential_properties or nonreferential_ok:
            pprint({k: v for k, v in self.alias2ents.items() if "Response" not in k})
            print()

    def dealias_property_reference(self, ref: Reference) -> Reference:
        """Substitute the aliased entity, which has the format
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

    def property_match(self) -> None:
        """After the reference-based alias-to-entity resolution, resolve remaining aliases
        by matching the properties of each alias to those of unified API definitions.

        Can match via total number of properties/property names/property descriptions.
        """
        for entity_alias in self.entity_schemas:
            if self.alias2ents[entity_alias] != []:
                continue
            property_count = next(
                count
                for count, entities in self.ents_by_property_count.items()
                if entity_alias in entities
            )
            candidates = self.unified_schema.ents_by_property_count[property_count]
            if len(candidates) > 1:
                if property_count > 0:
                    properties_to_match = list(
                        self.entity_schemas[entity_alias]["properties"],
                    )
                    property_lookup = {
                        entity: self.unified_schema.entity_schemas[entity]["properties"]
                        for entity in candidates
                    }
                    matched = {
                        entity: properties
                        for entity, properties in property_lookup.items()
                        if list(properties) == properties_to_match
                    }
                    if len(matched) > 0:
                        candidates = matched
            # else IDK
            if len(candidates) == 1:
                entity_name = next(iter(candidates))
                logger.debug(f"[PM] Established {entity_alias} == {entity_name}")
                self.resolve_alias(alias=entity_alias, entity=entity_name)

    def prepare_inventories(self) -> None:
        """Set the ``unified_schema`` as the unified API schema.

        Set up empty inventories keyed by the source entity alias:
        - to lists of the 'proper' entity names in the unified schema
        - to lists of the schema property references (initial)
        - to lists of the schema property references ('resolved' or 'dealiased')
        """
        self.unified_schema = single_unified_api_schema
        self.alias2ents: ApiAliasToUnifiedEntities = {
            alias: [] for alias in self.entity_schemas
        }
        self.property_refs: AliasToRefs = {alias: [] for alias in self.entity_schemas}
        self.resolved_property_refs: AliasToRefs = deepcopy(self.property_refs)
        self.resolution_counts = dict.fromkeys(self.entity_schemas, 0)
        """
        Extends the property refs lists for each alias in ``property_refs`` dict,
        then when ``resolve_refs`` is called for the alias which dealiases
        the property reference for any that are completable, stores the
        ``resolved_property_refs`` in a separate dict similar to
        ``property_refs``, then returns the number of refs 'completed'/resolved.
        """

    @property
    def any_referential_properties(self) -> bool:
        """If any of the API schema component properties included a reference to another
        entity, then the values of the ``property_refs`` dict will be non-empty.
        """
        return any(v for v in self.property_refs.values())
