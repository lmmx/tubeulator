from __future__ import annotations

__all__ = ["ApiInventory", "NamespaceInventory"]

class ApiEntity(str):
    """
    An API entity (typically an alias of the form "Tfl", "Tfl-1", "Tfl-2", etc.) from a
    non-unified API.
    """

class UnifiedApiEntity(str):
    """
    An API entity from the unified API
    """

ApiInventory = dict[ApiEntity, UnifiedApiEntity]
"""
An inventory of API entity (aliases) and the properly named entities they correspond to
from the unified API.
"""

NamespaceInventories = dict[ApiName, ApiInventory]
"""
The namespace of all APIs and their inventories mapping each of their API entities
(aliases) to the properly named entities they correspond to from the unified API.
"""
