#!/usr/bin/env bash

set -e  # exit immediately if a command fails

echo "Creating project structure"

# creating the directories
mkdir -p data
mkdir -p data/assets
mkdir -p data/pdfs
mkdir -p data/texts
mkdir -p tests
mkdir -p src
mkdir -p src/rag_app
mkdir -p src/rag_app/ui
mkdir -p src/rag_app/ui/build_ui
mkdir -p src/rag_app/ui/config
mkdir -p src/rag_app/ui/read_config
mkdir -p src/rag_app/config
mkdir -p src/rag_app/document_ingestion
mkdir -p src/rag_app/vectorstore
mkdir -p src/rag_app/llms
mkdir -p src/rag_app/state
mkdir -p src/rag_app/nodes
mkdir -p src/rag_app/graph_builder

echo "Creating files"

# root files
touch .env
touch pyproject.toml

# package files
touch src/rag_app/main.py
touch src/rag_app/app.py
touch src/rag_app/cli.py
touch src/rag_app/__init__.py

# subpackage init files
touch src/rag_app/ui/__init__.py
touch src/rag_app/ui/streamlit_ui/__init__.py
touch src/rag_app/config/__init__.py
touch src/rag_app/document_ingestion/__init__.py
touch src/rag_app/vectorstore/__init__.py
touch src/rag_app/llms/__init__.py
touch src/rag_app/state/__init__.py
touch src/rag_app/nodes/__init__.py
touch src/rag_app/graph_builder/__init__.py

# subpackage files
touch src/rag_app/ui/config/uiconfig.ini
touch src/rag_app/ui/config/ui_config.toml
touch src/rag_app/ui/read_config/read_from_ini.py
touch src/rag_app/ui/read_config/read_from_toml.py
touch src/rag_app/ui/build_ui/load_ui.py
touch src/rag_app/ui/build_ui/display_result.py

# tests
touch tests/__init__.py
touch tests/test_cli.py

echo "Project scaffold created successfully!"


