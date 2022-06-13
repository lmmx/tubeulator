from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import ujson

__all__ = ["ApiSchema"]


@dataclass
class ApiSchema:
    path: Path
    unified: bool

    def __post_init__(self):
        if self.path.suffix != ".json":
            raise ValueError(f"{self.path=} is not a JSON file")
        self.obj = ujson.loads(self.path.read_text())
        # Discard any of the entities with 'Array' in, they're not useful
        self.entity_schemas = {
            name: schema
            for name, schema in self.obj["components"].get("schemas", {}).items()
            if "Array" not in name
        }

    @property
    def name(self) -> str:
        return self.path.stem
