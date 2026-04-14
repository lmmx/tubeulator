#!/bin/bash
set -euo pipefail
export PATH="$HOME/.local/bin:$PATH"

echo "PYTHON VERSION"
uv run --no-sync python --version

echo "MKDOCS BUILD"
uv run --no-sync mkdocs build -v
