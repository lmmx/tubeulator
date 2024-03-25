from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import orjson

__all__ = ["ApiSchema"]


@dataclass
class ApiSchema:
    path: Path
    unified: bool

    def __post_init__(self):
        if self.path.suffix != ".json":
            raise ValueError(f"{self.path=} is not a JSON file")
        obj = orjson.loads(self.path.read_text())
        # Discard any of the entities with 'Array' in, they're not useful
        self.entity_schemas = {}
        self.ents_by_property_count = {}
        # self.entity_property_counts_inv = {}
        for name, schema in obj["components"].get("schemas", {}).items():
            # if self.is_skipped_name(name=name):
            #     continue
            self.entity_schemas[name] = schema
            property_count = len(schema.get("properties", []))
            # self.entity_property_counts[name] = property_count
            self.ents_by_property_count.setdefault(property_count, [])
            self.ents_by_property_count[property_count].append(name)

    @property
    def name(self) -> str:
        return self.path.stem

    # def is_skipped_name(self, name: str) -> bool:
    #    return "Array" in name
