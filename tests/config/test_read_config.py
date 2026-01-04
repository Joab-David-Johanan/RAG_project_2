import pytest
from rag_app.ui.read_config.read_from_toml import Config

def test_valid_toml(tmp_path):
    p = tmp_path / "config.toml"
    p.write_text("""
    [ui]
    page_title = "Test"
    chat_title = "Chat"

    [ui.options]
    llm_options = ["Groq"]
    usecase_options = ["Basic Chatbot"]

    [models]
    groq_model_options = ["groq-test"]
    openai_model_options = ["gpt-test"]
    """)

    cfg = Config(str(p))
    assert cfg.get_page_title() == "Test"

