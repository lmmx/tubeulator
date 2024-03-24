from pathlib import Path

from .. import generated
from ..openapi.scan import count_namespace
from .gen import emit_deserialisers

__all__ = ["generate_schema_coverage"]

codegen_dir = Path(generated.__file__).parent

schema_names = sorted(count_namespace(ignore_responses=True), key=str.lower)
schema_module_names = [f"{schema}.py".replace("-", "") for schema in schema_names]


def generate_schema_coverage():
    for schema_module, schema_name in zip(schema_module_names, schema_names):
        module_code = emit_deserialisers(schema_name=schema_name)
        module_filepath = codegen_dir / schema_module
        module_filepath.write_text(module_code)
