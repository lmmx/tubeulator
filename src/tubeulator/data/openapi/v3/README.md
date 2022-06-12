# TfL Open API (v3) JSON

Files for all of the APIs except 
the Unified API (which was legacy)
and the separate API listed for v1 of the Lifts API.

**Edit**: the unified API has been included in a subdirectory so as to distinguish it simply when
iterating over the APIs. It can be used to determine names for the entities in each API.

Obtained manually (download on each API page by clicking the _API definition_ dropdown menu).
Notably these differ from the v1 Swagger JSON file, containing fewer errors.
These errors are accounted for in the file [error_inventory.md](error_inventory.md).

The APIs were split out from a single unified API,
and in doing so lost their informative entity names.
It'd be desirable to recover these names, and appears to indeed be possible,
as covered in the file [naming.md](naming.md).
