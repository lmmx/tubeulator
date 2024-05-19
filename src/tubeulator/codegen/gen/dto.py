import ast
import textwrap
from itertools import starmap
from typing import Literal

from ...openapi.scan import scan_namespace
from ...utils.paths import SchemaPath
from ...utils.schemas import load_endpoint_component_schemas
from ...utils.string_conv import to_pascal_case
from .jsonschema import python_type
from .resolution import (
    find_array_literals,
    find_arrays,
    find_backrefs,
    find_chased,
    find_string_literals,
)

__all__ = [
    "import_node",
    "generate_dataclass_name",
    "generate_dataclass",
    "hidden_field",
    "generate_source",
]

GenModes = Literal["patito", "pydantic", "jsonw"]


def import_node(module: str, names: list[str]) -> ast.Import:
    if names:
        return ast.ImportFrom(module=module, names=[*map(ast.alias, names)], level=0)
    else:
        return ast.Import(names=[ast.alias(name=module)])


def generate_dataclass_name(
    schema: dict,
    name: str,
    source_schema_name: str,
    idx: int = None,
    dealiased_name: str | None = None,
    indent_level: int = 1,
) -> str | None:
    name, _ = generate_dataclass(
        schema=schema,
        name=name,
        source_schema_name=source_schema_name,
        idx=idx,
        dealiased_name=dealiased_name,
        indent_level=indent_level,
        schema_mapping=None,
        name_only=True,
    )
    return name


def generate_dataclass(
    schema: dict,
    name: str,
    source_schema_name: str,
    idx: int = None,
    dealiased_name: str | None = None,
    indent_level: int = 1,
    schema_mapping: dict[str, str] | None = None,
    name_only: bool = False,
) -> tuple[str, str] | tuple[None, None]:
    """Generate a dataclass from a schema, importing the `field` function if there are any
    array properties requiring it. Use the `idx` to indicate if we're generating
    multiple dataclasses in a loop. (TODO: replace with `schema: dict or list[dict]`).

    Either returns the name and the source, or None twice.
    """
    parent_schema = load_endpoint_component_schemas(source_schema_name)
    # ref may be None indicating schema may be {'type': 'object'}
    ref = schema.get("items", {}).get("$ref")
    ref_name = None if ref is None else SchemaPath(schema).ref.name
    backrefs = find_backrefs(parent_schema)
    schema_arrays = find_array_literals(parent_schema)
    schema_array_shortlist = find_arrays(list(schema_arrays))
    schema_strings = find_string_literals(parent_schema)
    schema_string_shortlist = find_arrays(list(schema_strings))
    # For Search, we also need to match Response DTOs without refs
    # For this we need to look for any arrays, not just $ref items
    # Chase the references if needed
    chased = find_chased(backrefs, name=name, ref_name=ref_name)
    app_infix = "Application"
    json_suffix = "JsonResponse"
    aj_suffix = f"{app_infix}{json_suffix}"
    response_shortlist = [c for c in chased if aj_suffix in c]
    if any("Array" in c for c in chased):
        array_shortlist = find_arrays(chased)
    else:
        array_shortlist = []
    assert not (response_shortlist and array_shortlist), "Got both Response and Array"
    if chased:
        # Multiple map to the node: they will be different response types
        assert response_shortlist or array_shortlist, "Neither Response nor Array found"
        if response_shortlist:
            if name not in response_shortlist:
                return None, None
            chase_prefixes = [
                p[: -len(aj_suffix)] for p in chased if p.endswith(aj_suffix)
            ]
            # old_chase_prefix = "_or_".join(chase_prefixes)  # Hotfix
            if len(chase_prefixes) > 1:
                chase_prefix = chase_prefixes[response_shortlist.index(name)]
            else:
                chase_prefix = chase_prefixes[0] if chase_prefixes else ""
            class_name = f"{chase_prefix}{aj_suffix}"
            gen_source = name  # ref_name
        else:
            if name not in array_shortlist:
                # Don't bother generating source for non-shortlisted array literals
                # it would only give None anyway
                return None, None
            ar_suffix = "Array"
            chase_prefixes = [
                p[: p.index(ar_suffix)] for p in chased if p in array_shortlist
            ]
            chase_prefix = "_or_".join(chase_prefixes)  # Hotfix: never used
            class_name = f"{chase_prefix}{ar_suffix}"
            gen_source = name  # ref_name
    elif dealiased_name is not None:
        stem = dealiased_name.rsplit(".", 1)[-1]
        class_name = f"{stem}"
        gen_source = dealiased_name
    elif (name, ref) != (None, None):
        # If they have a name but it's not in namespace, they're a response (targeting $ref)
        ns = scan_namespace(ignore_responses=True)
        if ref_name:
            if ref_lookup := ns[source_schema_name].get(ref_name, [None]):
                dealiased_ref = (ref_lookup)[0] or source_schema_name
            else:
                # The list of namespace lookups is empty
                dealiased_ref = source_schema_name
            # referent_class_name = f'{dealiased_ref.rsplit(".", 1)[-1]}'
            class_name = f'{dealiased_ref.rsplit(".", 1)[-1]}Response'
            gen_source = ref_name
        elif name in schema_arrays:
            if name not in schema_array_shortlist:
                return None, None
            short_delim = "Get200"
            shortname = name[: name.find(short_delim)] if short_delim in name else name
            class_name = f"{shortname}"
            gen_source = name
        else:
            if name in schema_strings and name not in schema_string_shortlist:
                return None, None
            # Essentially 'Unknown' f"UNK_{name}"
            class_name = f"{name}"
            gen_source = name
    else:
        gen_source = f"{source_schema_name}:{idx}"
        class_name = f"{source_schema_name}{idx if idx is not None else ''}"
        # class_name = source_schema_name.replace(" ", "")
    ent_prefix = "TflApiPresentationEntities"
    # Unslug the class name
    preproc_class_name = class_name.replace("-", "").replace(".", "")
    # Remove the long-winded entity prefix from the class name
    preproc_class_name = preproc_class_name[
        len(ent_prefix) if preproc_class_name.startswith(ent_prefix) else 0 :
    ]
    if name_only:
        output = None
    else:
        output = generate_source(
            class_name=preproc_class_name,
            component_name=name,
            schema_name=source_schema_name,
            gen_source=gen_source,
            schema=schema,
            parent_schema=parent_schema,
            indent_level=indent_level,
            idx=idx,
            schema_mapping=schema_mapping,
        )
    return preproc_class_name, output


def hidden_field(default_value: str, style: GenModes) -> str:
    if style == "jsonw":
        value = f"field(default={default_value!r}, repr=False)"
    elif style in ["patito", "pydantic"]:
        value = f"PrivateAttr(default={default_value!r})"
    return value


def make_class_header(class_name: str, style: GenModes) -> str:
    if style == "jsonw":
        hed = f"@dataclass\nclass {class_name}(JSONWizard):\n"
    elif style == "pydantic":
        hed = f"class {class_name}(BaseModel):\n"
    elif style == "patito":
        hed = f"class {class_name}(Model):\n"
    return hed


def generate_source(
    class_name: str,
    component_name: str,
    schema_name: str,
    gen_source: str,
    schema: dict,
    parent_schema: dict,
    indent_level: int,
    idx: int,
    schema_mapping: dict[str, str] | None,
    style: GenModes = "pydantic",
) -> str:
    is_jsonw = style == "jsonw"
    is_patito = style == "patito"
    is_pydantic = style in ["patito", "pydantic"]  # Careful: patito subclasses Pydantic
    properties = schema.get("properties", {})
    required = schema.get("required", [])
    contains_list = False
    dc_source = make_class_header(class_name=class_name, style=style)
    docstring = f"Autogenerated from {schema_name}::{gen_source}"
    dc_source += textwrap.indent(f'"""\n{docstring}\n"""\n', " " * indent_level * 4)
    if is_pydantic:
        alias_gen = "alias_generator=AliasGenerator(validation_alias=to_camel_case),"
        model_config = f"model_config = ConfigDict(\n    {alias_gen}\n)"
        dc_source += textwrap.indent(f"\n{model_config}\n\n", " " * indent_level * 4)
    for prop_name, prop_schema in properties.items():
        is_substituted = (
            "type" not in prop_schema and prop_schema and "$ref" in prop_schema
        )
        if is_substituted:
            referent = prop_schema["$ref"].replace("#/components/schemas/", "")
            replacement = parent_schema[referent]
            # Substitute the reference before accessing the item type
            # prop_schema["items"] = replacement
            # I don't think it handles nested dataclass arrays!
            # Don't in fact even need to replace in the schema, just the var
            prop_schema = replacement
            # (We could dealias the entity at this point so as to title it?)
        prop_type = python_type(prop_schema["type"], prop_schema.get("format"))
        is_array_prop = prop_schema["type"] == "array"
        if is_substituted:
            prop_type = schema_mapping[referent]
        if is_array_prop and "items" in prop_schema:
            prop_array = prop_schema["items"]
            # TODO: I think arrays should be handled at level above, check this sooner?
            if "type" not in prop_array and prop_array and "$ref" in prop_array:
                referent = prop_array["$ref"].replace("#/components/schemas/", "")
                # TODO: Don't substitute: look up using Deserialisers Enum
                # replacement = parent_schema[referent]
                dto_enum_lookup = f"Deserialisers[{referent}].value"
                if schema_mapping is None:
                    item_type = dto_enum_lookup
                else:
                    item_type = schema_mapping.get(referent, dto_enum_lookup)
                    if is_pydantic:
                        # Important: stringify to postpone field's schema resolution
                        # (premature access will lead to PydanticSchemaGenerationError)
                        item_type = f'"{item_type}Model"'
                # Substitute the reference before accessing the item type
                # prop_schema["items"] = replacement
                # I don't think it handles nested dataclass arrays!
                # Don't in fact even need to replace in the schema, just the var
                # prop_array = replacement
                # (We could dealias the entity at this point so as to title it?)
            else:
                item_type = python_type(prop_array["type"], prop_array.get("format"))
            prop_type = f"{prop_type}[{item_type}]"
        elif is_pydantic and is_substituted:
            prop_type = f"{prop_type}Model"
        if prop_name in required:
            default = ""
        else:
            if is_array_prop:
                contains_list = True
                if is_pydantic:
                    default = " = []"
                else:
                    default = " = field(default_factory=list)"
            else:
                default = " = None"
        dc_source += f"    {to_pascal_case(prop_name)}: {prop_type}{default}\n"
    source_schema_default = hidden_field(schema_name, style=style)
    component_default = hidden_field(component_name, style=style)
    dc_source += f"    _source_schema_name: str = {source_schema_default}\n"
    dc_source += f"    _component_schema_name: str = {component_default}\n"
    jsonw_methods = """
    @classmethod
    def from_dict(cls, o):
        parent_schema = load_endpoint_component_schemas(cls._source_schema_name)
        schema = parent_schema[cls._component_schema_name]
        jsonschema.validate(o, schema)
        return fromdict(cls, o)

    class Meta(JSONWizard.Meta):
        key_transform_with_load = 'PASCAL'
        recursive_classes = True"""
    if is_jsonw:
        dc_source += jsonw_methods
    elif is_pydantic:
        # Patch field annotation bug https://github.com/pydantic/pydantic/issues/9093
        dc_source += f"\n\n{class_name}Model = {class_name}"
    jsonw_imports = {
        "dataclass_wizard": ["JSONWizard"],
        "dataclass_wizard.loaders": ["fromdict"],
        "jsonschema": [],
    }
    pydantic_imports = {
        "tubeulator.utils.string_conv": ["to_camel_case"],
        "pydantic": ["AliasGenerator", "BaseModel", "ConfigDict", "PrivateAttr"],
    }
    patito_imports = {
        "tubeulator.utils.string_conv": ["to_camel_case"],
        "patito": ["Model"],
        "pydantic": ["AliasGenerator", "ConfigDict", "PrivateAttr"],
    }
    jsonw_utils = ["load_endpoint_component_schemas"]
    pydantic_imports = patito_imports if is_patito else pydantic_imports
    import_list = {
        "__future__": ["annotations"],
        "json": [],
        "datetime": ["datetime"],
        "dataclasses": ["dataclass"],
        # "pathlib": ["Path"], # I think this was a mistake
        **(jsonw_imports if is_jsonw else {}),
        **(pydantic_imports if is_pydantic else {}),
        "..utils.paths": [
            *(jsonw_utils if is_jsonw else []),
            "DtoEnum",
        ],
    }
    if contains_list or idx == 0:
        import_list["dataclasses"].append("field")
    imports = "\n".join(map(ast.unparse, starmap(import_node, import_list.items())))
    # Add imports here if generating multiple dataclasses [indicated by idx=0] (since we
    # can't see ahead), or if only making 1 [indicated by idx=None]
    return "\n\n".join([(imports if not idx else ""), dc_source])
