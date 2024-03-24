import ast
from itertools import starmap


def python_type(json_type: str, format: str = None) -> str:
    """Map property types in the JSON schema to Python types for type annotation."""
    if json_type == "string":
        if format == "email":
            return "str"
        return "str"
    elif json_type == "integer":
        return "int"
    elif json_type == "boolean":
        return "bool"
    elif json_type == "array":
        return "list"
    elif json_type == "object":
        return "dict"
    else:
        return "Any"


def import_node(module: str, names: list[str]) -> ast.Import:
    if names:
        return ast.ImportFrom(
            module=module,
            names=[ast.alias(name=name) for name in names],
            level=0,
        )
    else:
        return ast.Import(names=[ast.alias(name=module)])


def generate_dataclass(schema: dict) -> str:
    """Generate a dataclass from a schema, importing the `field` function if there are any
    array properties requiring it.
    """
    import_list = {
        "json": [],
        "dataclasses": ["dataclass"],
        "pathlib": ["Path"],
        "dataclass_wizard": ["JSONWizard", "LoadMeta"],
        "dataclass_wizard.loaders": ["fromdict"],
        "jsonschema": [],
    }
    class_name = schema.get("title", "UntitledDataclass").replace(" ", "")
    properties = schema.get("properties", {})
    required = schema.get("required", [])
    contains_list = False
    dc_source = "@dataclass\n"
    dc_source += f"class {class_name}(JSONWizard):\n"
    for prop_name, prop_schema in properties.items():
        prop_type = python_type(prop_schema["type"], prop_schema.get("format"))
        is_array_prop = prop_schema["type"] == "array"
        if is_array_prop and "items" in prop_schema:
            item_type = python_type(prop_schema["items"]["type"])
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
    if contains_list:
        import_list["dataclasses"].append("field")
    imports = "\n".join(map(ast.unparse, starmap(import_node, import_list.items())))
    meta_binding = f"LoadMeta(raise_on_unknown_json_key=True).bind_to({class_name})"
    output = "\n\n".join([imports, dc_source, meta_binding])
    return output


schema = {
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

generated_code = generate_dataclass(schema)
print(generated_code)
