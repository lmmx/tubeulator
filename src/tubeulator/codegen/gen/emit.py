"""Emit DTO code generated for TfL APIs (detected from their loaded Swagger schemas)."""

from ...openapi.scan import scan_namespace
from ...utils.paths import to_enum_friendly_str
from ...utils.schemas import load_endpoint_component_schemas
from .dto import generate_dataclass, generate_dataclass_name
from .helpers import logger

__all__ = ["emit_deserialisers"]


def emit_deserialisers(schema_name: str) -> str:
    """Generate the source code for a module with DTOs for an entire TfL schema."""
    component_schemas = load_endpoint_component_schemas(schema_name)
    ns = scan_namespace(ignore_responses=True)
    output = []
    schema_mapping = {}
    # 1st pass for the generated dataclass names (populating the schema mapping)
    for idx, (component_name, component_schema) in enumerate(component_schemas.items()):
        true_name = (ns.get(schema_name, {}).get(component_name) or [None])[0]
        try:
            generated_class_name = generate_dataclass_name(
                component_schema,
                name=component_name,
                source_schema_name=schema_name,
                idx=idx,
                dealiased_name=true_name,
            )
            if generated_class_name is not None:
                schema_mapping.setdefault(component_name, generated_class_name)
        except Exception as e:
            logger.error(
                f"Failed to generate name for {schema_name} dataclass {idx}: "
                f"{component_name} (dealiased: {true_name}) -- {e}",
                exc_info=True,
            )
    # 2nd pass for the source code (using the schema mapping)
    for idx, (component_name, component_schema) in enumerate(component_schemas.items()):
        true_name = (ns.get(schema_name, {}).get(component_name) or [None])[0]
        try:
            generated_class_name, generated_code = generate_dataclass(
                component_schema,
                name=component_name,
                source_schema_name=schema_name,
                idx=idx,
                dealiased_name=true_name,
                schema_mapping=schema_mapping,
            )
            output.append(generated_code)  # Append even if None, for debugging purposes
        except Exception as e:
            logger.error(
                f"Failed to generate {schema_name} dataclass {idx}: "
                f"{component_name} (dealiased: {true_name}) -- {e}",
                exc_info=True,
            )
    deserialiser_code = "\n".join(filter(None, output))
    if deserialiser_code:
        schema_mapping_source = "\n\n\nclass Deserialisers(DtoEnum):\n" + "\n".join(
            [
                f"    {to_enum_friendly_str(component_name)} = {cls_name}"
                for component_name, cls_name in schema_mapping.items()
            ],
        )
        deserialiser_code += schema_mapping_source
    return deserialiser_code
