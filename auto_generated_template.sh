#!/usr/bin/env bash

set -e  # exit immediately if a command fails

echo "Creating project structure"

# creating the directories
mkdir -p .
mkdir -p data
mkdir -p src
mkdir -p src/rag_app
mkdir -p src/rag_app.egg-info
mkdir -p src/rag_app/controller
mkdir -p src/rag_app/core
mkdir -p src/rag_app/core/graph_builder
mkdir -p src/rag_app/core/ingestion
mkdir -p src/rag_app/core/nodes
mkdir -p src/rag_app/core/state
mkdir -p src/rag_app/core/vectorstore
mkdir -p src/rag_app/llms
mkdir -p src/rag_app/ui
mkdir -p src/rag_app/ui/build_ui
mkdir -p src/rag_app/ui/config
mkdir -p src/rag_app/ui/read_config
mkdir -p tests

echo "Creating files"

# python + config files
touch .streamlit/config.toml
touch pyproject.toml
touch src/rag_app/__init__.py
touch src/rag_app/app.py
touch src/rag_app/controller/__init__.py
touch src/rag_app/controller/app_controller.py
touch src/rag_app/controller/graph_controller.py
touch src/rag_app/controller/output_controller.py
touch src/rag_app/controller/ui_controller.py
touch src/rag_app/core/graph_builder/__init__.py
touch src/rag_app/core/graph_builder/basic_chatbot_graph.py
touch src/rag_app/core/ingestion/__init__.py
touch src/rag_app/core/nodes/__init__.py
touch src/rag_app/core/nodes/basic_chatbot_node.py
touch src/rag_app/core/state/__init__.py
touch src/rag_app/core/state/basic_chatbot_state.py
touch src/rag_app/core/vectorstore/__init__.py
touch src/rag_app/llms/__init__.py
touch src/rag_app/llms/groq_llm.py
touch src/rag_app/llms/openai_llm.py
touch src/rag_app/llms/route_correct_llm.py
touch src/rag_app/main.py
touch src/rag_app/ui/__init__.py
touch src/rag_app/ui/build_ui/__init__.py
touch src/rag_app/ui/build_ui/load_conversation.py
touch src/rag_app/ui/build_ui/load_sidebar.py
touch src/rag_app/ui/config/config_schema.py
touch src/rag_app/ui/config/uiconfig.ini
touch src/rag_app/ui/config/uiconfig.toml
touch src/rag_app/ui/read_config/read_from_ini.py
touch src/rag_app/ui/read_config/read_from_toml.py
touch tests/__init__.py

echo "Project scaffold created successfully!"
