import ast
import json
from itertools import starmap
from pathlib import Path

from .utils.paths import find_schema_by_name

__all__ = ["emit_deserialisers"]


def python_type(json_type: str, format: str = None) -> str:
    """
    Map property types in the JSON schema to Python types for type annotation.
    The `format` can be "email" if it's a string but it doesn't change the result.
    """
    type_lookup = {
        "string": "str",
        "integer": "int",
        "boolean": "bool",
        "array": "list",
        "object": "dict",
    }
    return type_lookup.get(json_type, "Any")


def import_node(module: str, names: list[str]) -> ast.Import:
    if names:
        return ast.ImportFrom(module=module, names=[*map(ast.alias, names)], level=0)
    else:
        return ast.Import(names=[ast.alias(name=module)])


def generate_dataclass(
    schema: dict, idx: int = None, schema_for_ref_lookup: dict | None = None
) -> str:
    """
    Generate a dataclass from a schema, importing the `field` function if there are any
    array properties requiring it. Use the `idx` to indicate if we're generating
    multiple dataclasses in a loop. (TODO: replace with `schema: dict or list[dict]`)
    """
    import_list = {
        "json": [],
        "dataclasses": ["dataclass"],
        "pathlib": ["Path"],
        "dataclass_wizard": ["JSONWizard", "LoadMeta"],
        "dataclass_wizard.loaders": ["fromdict"],
        "jsonschema": [],
    }
    class_name = schema.get("title", "Untitled").replace(" ", "") + "Deserialiser"
    properties = schema.get("properties", {})
    required = schema.get("required", [])
    contains_list = False
    dc_source = "@dataclass\n"
    dc_source += f"class {class_name}(JSONWizard):\n"
    for prop_name, prop_schema in properties.items():
        if "type" not in prop_schema:
            if prop_schema and "$ref" in prop_schema:
                referent = prop_schema["$ref"].replace("#/components/schemas/", "")
                replacement = schema_for_ref_lookup[referent]
                # Substitute the reference before accessing the item type
                # prop_schema["items"] = replacement
                # breakpoint() # I don't think it handles nested dataclass arrays!
                # Don't in fact even need to replace in the schema, just the var
                prop_schema = replacement
                # (We could dealias the entity at this point so as to title it?)
        prop_type = python_type(prop_schema["type"], prop_schema.get("format"))
        is_array_prop = prop_schema["type"] == "array"
        if is_array_prop and "items" in prop_schema:
            prop_array = prop_schema["items"]
            # TODO: I think arrays should be handled at level above, check this sooner?
            if "type" not in prop_array:
                if prop_array and "$ref" in prop_array:
                    referent = prop_array["$ref"].replace("#/components/schemas/", "")
                    replacement = schema_for_ref_lookup[referent]
                    # Substitute the reference before accessing the item type
                    # prop_schema["items"] = replacement
                    # breakpoint() # I don't think it handles nested dataclass arrays!
                    # Don't in fact even need to replace in the schema, just the var
                    prop_array = replacement
                    # (We could dealias the entity at this point so as to title it?)
            item_type = python_type(prop_array["type"])
            prop_type = f"{prop_type}[{item_type}]"
        if prop_name in required:
            default = ""
        else:
            if is_array_prop:
                contains_list = True
                default = " = field(default_factory=list)"
            else:
                default = " = None"
        dc_source += f"    {prop_name}: {prop_type}{default}\n"
    dc_source += """    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)"""
    if contains_list or idx == 0:
        import_list["dataclasses"].append("field")
    imports = "\n".join(map(ast.unparse, starmap(import_node, import_list.items())))
    meta_binding = f"\nLoadMeta(raise_on_unknown_json_key=True).bind_to({class_name})"
    # Add imports here if generating multiple dataclasses [indicated by idx=0] (since we
    # can't see ahead), or if only making 1 [indicated by idx=None]
    output = "\n\n".join([(imports if not idx else ""), dc_source, meta_binding])
    return output


example_schema = {
    "title": "Example Schema",
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "integer"},
        "email": {"type": "string", "format": "email"},
        "friends": {"type": "array", "items": {"type": "string"}},
    },
    "required": ["name", "age"],
}


def emit_deserialisers(schema_name: str) -> None:
    endpoint_schema = json.loads(Path(find_schema_by_name(schema_name)).read_text())
    component_schemas = endpoint_schema["components"].get("schemas", {})
    for idx, (component_name, component_schema) in enumerate(component_schemas.items()):
        generated_code = generate_dataclass(
            component_schema, idx=idx, schema_for_ref_lookup=component_schemas
        )
        print(generated_code)
    return
