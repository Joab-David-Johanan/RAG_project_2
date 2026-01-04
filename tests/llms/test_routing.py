import pytest
from rag_app.llms.route_correct_llm import RouteLLM

class DummyChoices:
    def __init__(self, selected_llm):
        self.selected_llm = selected_llm

def test_route_groq(monkeypatch):
    monkeypatch.setenv("GROQ_API_KEY", "fake-key")

    monkeypatch.setattr(
        "rag_app.llms.groq_llm.ChatGroq",
        lambda model: f"mocked-{model}"
    )

    user_choices = {
        "selected_llm": "Groq",
        "selected_groq_model": "groq-test-model",
    }

    rr = RouteLLM(user_choices)
    llm = rr.get_llm()

    assert llm == "mocked-groq-test-model"

def test_route_unknown_raises():
    user_choices = {"selected_llm": "NotAnOption"}
    with pytest.raises(ValueError):
        RouteLLM(user_choices).get_llm()
