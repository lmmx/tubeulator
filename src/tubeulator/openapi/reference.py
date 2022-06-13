from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from ._types import ApiAliasToUnifiedEntities, EntityURI

__all__ = [
    "Reference",
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
