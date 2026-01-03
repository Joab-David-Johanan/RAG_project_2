#!/usr/bin/env bash

set -e  # exit immediately if a command fails

echo "Creating project structure"

# creating the directories
mkdir -p .
mkdir -p data
mkdir -p src
mkdir -p src/rag_app
mkdir -p src/rag_app.egg-info
mkdir -p src/rag_app/__pycache__
mkdir -p src/rag_app/config
mkdir -p src/rag_app/controller
mkdir -p src/rag_app/controller/__pycache__
mkdir -p src/rag_app/document_ingestion
mkdir -p src/rag_app/graph_builder
mkdir -p src/rag_app/graph_builder/__pycache__
mkdir -p src/rag_app/llms
mkdir -p src/rag_app/llms/__pycache__
mkdir -p src/rag_app/nodes
mkdir -p src/rag_app/nodes/__pycache__
mkdir -p src/rag_app/state
mkdir -p src/rag_app/state/__pycache__
mkdir -p src/rag_app/ui
mkdir -p src/rag_app/ui/__pycache__
mkdir -p src/rag_app/ui/build_ui
mkdir -p src/rag_app/ui/build_ui/__pycache__
mkdir -p src/rag_app/ui/config
mkdir -p src/rag_app/ui/config/__pycache__
mkdir -p src/rag_app/ui/read_config
mkdir -p src/rag_app/ui/read_config/__pycache__
mkdir -p src/rag_app/vectorstore
mkdir -p tests

echo "Creating files"

# python + config files
touch .streamlit/config.toml
touch pyproject.toml
touch src/rag_app/__init__.py
touch src/rag_app/app.py
touch src/rag_app/cli.py
touch src/rag_app/config/__init__.py
touch src/rag_app/controller/__init__.py
touch src/rag_app/controller/app_controller.py
touch src/rag_app/controller/graph_controller.py
touch src/rag_app/controller/output_controller.py
touch src/rag_app/controller/ui_controller.py
touch src/rag_app/document_ingestion/__init__.py
touch src/rag_app/graph_builder/__init__.py
touch src/rag_app/graph_builder/basic_chatbot_graph.py
touch src/rag_app/llms/__init__.py
touch src/rag_app/llms/groq_llm.py
touch src/rag_app/llms/openai_llm.py
touch src/rag_app/llms/route_correct_llm.py
touch src/rag_app/main.py
touch src/rag_app/nodes/__init__.py
touch src/rag_app/nodes/basic_chatbot_node.py
touch src/rag_app/state/__init__.py
touch src/rag_app/state/basic_chatbot_state.py
touch src/rag_app/ui/__init__.py
touch src/rag_app/ui/build_ui/__init__.py
touch src/rag_app/ui/build_ui/load_conversation.py
touch src/rag_app/ui/build_ui/load_sidebar.py
touch src/rag_app/ui/config/config_schema.py
touch src/rag_app/ui/config/uiconfig.ini
touch src/rag_app/ui/config/uiconfig.toml
touch src/rag_app/ui/read_config/read_from_ini.py
touch src/rag_app/ui/read_config/read_from_toml.py
touch src/rag_app/vectorstore/__init__.py
touch tests/__init__.py
touch tests/test_cli.py

echo "Project scaffold created successfully!"
