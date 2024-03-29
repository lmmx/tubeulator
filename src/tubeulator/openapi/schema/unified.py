from __future__ import annotations

from ...utils.schemas import unified_api_schema
from .base import ApiSchema

__all__ = [
    "UnifiedApiSchema",
    "single_unified_api_schema",
]


class UnifiedApiSchema(ApiSchema):
    """A unified API schema."""

    unified: bool = True


single_unified_api_schema = UnifiedApiSchema(path=unified_api_schema, unified=True)
"""
A singleton instance to avoid re-reading the unified API schema JSON once per
non-unified API schema instantiation.
"""
