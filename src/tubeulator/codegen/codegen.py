import ast
import json
import logging
import textwrap
from itertools import starmap
from pathlib import Path
from textwrap import indent

from dataclass_wizard.utils.string_conv import to_pascal_case

from ..openapi.scan import scan_namespace
from ..utils.lcp_trie import Trie
from ..utils.paths import (
    SchemaPath,
    find_schema_by_name,
    load_endpoint_component_schemas,
    to_enum_friendly_str,
)

__all__ = ["emit_deserialisers"]

logger = logging.getLogger(__name__)


class CustomFormatter(logging.Formatter):
    def formatException(self, exc_info):
        result = super().formatException(exc_info)
        return indent(
            f"\n{result}\n",
            prefix=" " * 8,
        )


formatter = CustomFormatter("[%(levelname)s] - %(message)s")

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)


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
    if json_type == "number" and format == "double":
        python_type = "float"
    elif json_type == "string" and format == "date-time":
        python_type = "datetime"
    else:
        python_type = type_lookup[json_type]
    return python_type


def import_node(module: str, names: list[str]) -> ast.Import:
    if names:
        return ast.ImportFrom(module=module, names=[*map(ast.alias, names)], level=0)
    else:
        return ast.Import(names=[ast.alias(name=module)])


def find_backrefs(monoschema: dict) -> dict[str, SchemaPath]:
    """
    Map names of all schemas in the lookup to their referent (i.e. their array type)
    """
    return {
        k: SchemaPath(v)
        for k, v in monoschema.items()
        if "items" in v
        if "$ref" in v["items"]
    }


def find_string_literals(monoschema: dict) -> dict[str, str]:
    """
    Map names of all schemas in the lookup with a common literal string.
    """
    return {k: v["type"] for k, v in monoschema.items() if v.get("type") == "string"}


def find_array_literals(monoschema: dict) -> dict[str, SchemaPath]:
    """
    Map names of all schemas in the lookup with a common literal array.
    """
    return {
        k: v["items"]["type"]
        for k, v in monoschema.items()
        if "type" in v.get("items", {})
    }


def find_chased(backrefs: dict[str, SchemaPath], name: str, ref_name: str) -> list[str]:
    return [
        backref
        for backref, schema_path in backrefs.items()
        if schema_path.ref.name == ref_name
    ]


def find_arrays(chased: list[str]) -> list[str]:
    """
    Can't simply choose the one(s) ending in 'Array': in Mode it ends in "Array-4"
    """
    t = Trie()
    for c in chased:
        t.insert(c)
    # array_shortlist = [c for c in chased if c.endswith("Array")]
    array_shortlist = []
    try:
        for stem, stem_node in t.root.data.items():
            if stem_node.is_word:
                array_shortlist.append(stem)
            else:
                substem, substem_node = next(iter(stem_node.data.items()))
                assert (
                    substem_node.is_word
                ), "Descended 2 trie levels and didn't get a word"
                array_shortlist.append(f"{stem}{substem}")
    except AssertionError:
        # It's an assortment of responses, just pull out the ones we want
        array_shortlist = [c for c in chased if "ApplicationJson" in c]
    return array_shortlist


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
    """
    Generate a dataclass from a schema, importing the `field` function if there are any
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
            old_chase_prefix = "_or_".join(chase_prefixes)  # Hotfix
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
            if name in schema_strings and not name in schema_string_shortlist:
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
    preproc_class_name = class_name.replace("-", "")
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
) -> str:
    properties = schema.get("properties", {})
    required = schema.get("required", [])
    contains_list = False
    dc_source = f"@dataclass\nclass {class_name}(JSONWizard):\n"
    docstring = f"Autogenerated from {schema_name}::{gen_source}"
    dc_source += textwrap.indent(f'"""\n{docstring}\n"""\n', " " * indent_level * 4)
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
                # Substitute the reference before accessing the item type
                # prop_schema["items"] = replacement
                # I don't think it handles nested dataclass arrays!
                # Don't in fact even need to replace in the schema, just the var
                # prop_array = replacement
                # (We could dealias the entity at this point so as to title it?)
            else:
                item_type = python_type(prop_array["type"], prop_array.get("format"))
            prop_type = f"{prop_type}[{item_type}]"
        if prop_name in required:
            default = ""
        else:
            if is_array_prop:
                contains_list = True
                default = " = field(default_factory=list)"
            else:
                default = " = None"
        dc_source += f"    {to_pascal_case(prop_name)}: {prop_type}{default}\n"
    dc_source += f"    _source_schema_name: str = {schema_name!r}\n"
    dc_source += f"    _component_schema_name: str = {component_name!r}\n"
    dc_source += """    
    @classmethod
    def from_dict(cls, o):
        parent_schema = load_endpoint_component_schemas(cls._source_schema_name)
        schema = parent_schema[cls._component_schema_name]
        jsonschema.validate(o, schema)
        return fromdict(cls, o)
    
    class Meta(JSONWizard.Meta):
        key_transform_with_load = 'PASCAL'
        recursive_classes = True"""
    import_list = {
        "__future__": ["annotations"],
        "json": [],
        "datetime": ["datetime"],
        "dataclasses": ["dataclass"],
        "pathlib": ["Path"],
        "dataclass_wizard": ["JSONWizard"],
        "dataclass_wizard.loaders": ["fromdict"],
        "jsonschema": [],
        "..utils.paths": ["load_endpoint_component_schemas", "DtoEnum"],
    }
    if contains_list or idx == 0:
        import_list["dataclasses"].append("field")
    imports = "\n".join(map(ast.unparse, starmap(import_node, import_list.items())))
    # Add imports here if generating multiple dataclasses [indicated by idx=0] (since we
    # can't see ahead), or if only making 1 [indicated by idx=None]
    return "\n\n".join([(imports if not idx else ""), dc_source])


def emit_deserialisers(schema_name: str) -> str:
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
            ]
        )
        deserialiser_code += schema_mapping_source
    return deserialiser_code
