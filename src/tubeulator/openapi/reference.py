from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass
from functools import reduce
from pathlib import Path

from ._types import ApiAliasToUnifiedEntities, ApiEntityAlias, EntityURI

__all__ = [
    "Reference",
    "AliasToRefs",
    "dealias_schema",
]


@dataclass
class Reference:
    schema: str
    alias: str
    referential_property: str
    # path: tuple[Literal["items","$ref"]]
    is_array: bool
    entity: EntityURI

    @property
    def path(self) -> tuple[str, ...]:
        return (*(["items"] if self.is_array else []), "$ref")

    @property
    def substituted_ref(self) -> str:
        return Path(self.entity).name

    def is_completable(self, api_inventory: ApiAliasToUnifiedEntities):
        """If the API inventory has a resolved value (or values) for the alias referenced
        in the current referential property's ``$ref`` key, then the reference can be
        resolved immediately (i.e. "completed"). If not, we have to wait for the next
        round of substitutions, or chase references.
        """
        if self.substituted_ref in api_inventory:
            return api_inventory[self.substituted_ref] != []
        else:
            raise ValueError(f"{self.substituted_ref=} not found in {api_inventory=}")


AliasToRefs = dict[ApiEntityAlias, list[Reference]]
"""
An inventory of API entity aliases and the references they contain.
"""


def dealias_schema(refs: list[Reference], component: dict, copy: bool = True) -> dict:
    """Modify the schema component of an API schema to overwrite the reference with
    the entity name in the :obj:`Reference` instead of the alias there.
    """
    if copy:
        component = deepcopy(component)
    for ref in refs:
        target_property = component["properties"][ref.referential_property]
        target_subpath = ref.path[:-1]
        target_leaf = ref.path[-1]
        target = reduce(dict.get, target_subpath, target_property)
        target[target_leaf] = ref.entity
    return component
