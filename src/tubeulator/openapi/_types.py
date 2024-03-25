from __future__ import annotations

__all__ = [
    "ApiName",
    "ApiEntityAlias",
    "UnifiedApiEntity",
    "ApiAliasToUnifiedEntities",
    "NamespaceInventory",
    "EntityURI",
]

ApiName = str
"""
The name of an API (which is also the stem of the API schema file itself).
"""


class ApiEntityAlias(str):
    """An API entity (typically an alias of the form "Tfl", "Tfl-1", "Tfl-2", etc.) from a
    non-unified API.
    """


class UnifiedApiEntity(str):
    """An API entity from the unified API"""


ApiAliasToUnifiedEntities = dict[ApiEntityAlias, list[UnifiedApiEntity]]
"""
An inventory of API entity aliases and the properly named entities they correspond to
from the unified API. Since there is no guarantee that different unified API entities
cannot have identical schemas, there may be a one-to-many mapping (i.e. the dict is
list-valued).
"""

NamespaceInventory = dict[ApiName, ApiAliasToUnifiedEntities]
"""
The namespace of all APIs and their inventories mapping each of their API entities
(aliases) to the properly named entities they correspond to from the unified API.
"""

EntityURI = str
