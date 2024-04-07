"""Functions for the unique resolution of schema identifiers."""

from ...utils.lcp_trie import Trie
from ...utils.paths import SchemaPath

__all__ = [
    "find_backrefs",
    "find_string_literals",
    "find_array_literals",
    "find_chased",
    "find_arrays",
]


def find_backrefs(monoschema: dict) -> dict[str, SchemaPath]:
    """Map names of all schemas in the lookup to their referent (i.e. their array type)"""
    return {
        k: SchemaPath(v)
        for k, v in monoschema.items()
        if "items" in v
        if "$ref" in v["items"]
    }


def find_string_literals(monoschema: dict) -> dict[str, str]:
    """Map names of all schemas in the lookup with a common literal string."""
    return {k: v["type"] for k, v in monoschema.items() if v.get("type") == "string"}


def find_array_literals(monoschema: dict) -> dict[str, SchemaPath]:
    """Map names of all schemas in the lookup with a common literal array."""
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
    """Can't simply choose the one(s) ending in 'Array': in Mode it ends in "Array-4" """
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
