from __future__ import annotations

from ...utils.paths import unified_api_schema as unified_api_schema_path
from .base import ApiSchema

__all__ = [
    "UnifiedApiSchema",
    "single_unified_api_schema",
]


class UnifiedApiSchema(ApiSchema):
    """A unified API schema."""

    unified: bool = True


single_unified_api_schema = UnifiedApiSchema(path=unified_api_schema_path, unified=True)
"""
A singleton instance to avoid re-reading the unified API schema JSON once per
non-unified API schema instantiation.
"""
