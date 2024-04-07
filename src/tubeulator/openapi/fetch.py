"""Download and store (overwrite) the OpenAPI JSON schemas for TfL APIs."""

import json

import httpx

from ..utils.paths import openapi_schemas_path

__all__ = ["fetch_schema"]


def fetch_schema(schema_name: str, api_version: str) -> str:
    """Fetch a TfL API OpenAPI JSON schema, pretty printing with indent=4."""
    export_url = f"https://api-portal.tfl.gov.uk/developer/apis/{schema_name}"
    headers = {"Accept": "application/vnd.oai.openapi+json"}
    params = {"export": True, "api-version": api_version}
    download = httpx.get(export_url, headers=headers, params=params)
    download.raise_for_status()
    pp_json = json.dumps(download.json(), indent=4)
    return pp_json


def refresh_schema(schema_name: str, api_version: str) -> None:
    """Store a TfL API OpenAPI JSON schema, overwriting if one exists."""
    schema_dir = openapi_schemas_path / schema_name
    schema_file = (schema_dir / schema_name).with_suffix(".json")
    schema_json = fetch_schema(schema_name=schema_name, api_version=api_version)
    if schema_file.exists():
        old_json = schema_file.read_text()
        old_file_size = len(old_json.splitlines())
        new_file_size = len(schema_json.splitlines())
        diff = f"{old_file_size} lines -> {new_file_size} lines"
        is_match = ""
        if old_file_size == new_file_size:
            if old_json.rstrip() == schema_json.rstrip():
                is_match = " -- no change"
        message = f"Writing {schema_file.name} ({diff}){is_match}"
    else:
        message = f"Writing {schema_file.name} (new file)"
    print(message)
    schema_file.write_text(schema_json)
    return
