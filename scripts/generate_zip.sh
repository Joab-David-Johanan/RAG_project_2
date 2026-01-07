#!/usr/bin/env bash

set -e

# Name of the output archive
OUT="RAG_project_2_repo.zip"

echo "Zipping the entire project into $OUT"

# -r : recursive
# -9 : maximum compression
# Exclude the virtualenv to keep it light
zip -r -9 "$OUT" . \
   -x "venv/*" \
   -x ".git/*" \
   -x "__pycache__/*"

echo "Done!"
echo "You can now export $OUT as a zip file."
