## End to End Agentic RAG Chatbot

### Project Structure

```text

RAG_project_2
├── data
│   ├── assets
│   │   ├── blue_transformer.png
│   │   └── red_transformer.png
│   ├── pdfs
│   │   └── WhoG-Flextime-Policy.pdf
│   ├── texts
│   └── vectorstore
├── scripts
│   ├── generate_template.sh
│   ├── generate_tree.sh
│   └── generate_zip.sh
├── src
│   └── rag_app
│       ├── app
│       │   ├── __init__.py
│       │   ├── app_controller.py
│       │   ├── graph_controller.py
│       │   ├── output_controller.py
│       │   └── ui_controller.py
│       ├── core
│       │   ├── graph
│       │   │   ├── __init__.py
│       │   │   └── build_graph.py
│       │   ├── ingestion
│       │   │   ├── __init__.py
│       │   │   └── document_processor.py
│       │   ├── nodes
│       │   │   ├── __init__.py
│       │   │   └── build_node.py
│       │   ├── schema
│       │   │   ├── __init__.py
│       │   │   └── build_state.py
│       │   └── vectorstore
│       │       ├── __init__.py
│       │       └── create_vectorstore.py
│       ├── llms
│       │   ├── __init__.py
│       │   ├── groq_llm.py
│       │   ├── openai_llm.py
│       │   └── route_correct_llm.py
│       ├── ui
│       │   ├── chat
│       │   │   ├── __init__.py
│       │   │   └── load_conversation.py
│       │   ├── config
│       │   │   ├── config_schema.py
│       │   │   ├── uiconfig.ini
│       │   │   └── uiconfig.toml
│       │   ├── pages
│       │   │   ├── __init__.py
│       │   │   ├── basic_chatbot_page.py
│       │   │   ├── homepage.py
│       │   │   └── rag_chatbot_page.py
│       │   ├── read_config
│       │   │   ├── read_from_ini.py
│       │   │   └── read_from_toml.py
│       │   ├── __init__.py
│       │   ├── router.py
│       │   └── theme.py
│       ├── __init__.py
│       ├── app.py
│       └── main.py
├── tests
│   ├── app
│   ├── config
│   │   └── test_read_config.py
│   ├── core
│   │   ├── test_graph.py
│   │   └── test_nodes.py
│   ├── llms
│   │   ├── test_openai_llm.py
│   │   └── test_routing.py
│   └── __init__.py
├── .env
├── .gitignore
├── README.md
├── auto_generated_template.sh
├── project_structure.txt
├── pyproject.toml
├── rag_app.code-workspace
└── requirements.txt


```
