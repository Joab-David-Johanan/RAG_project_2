from rag_app.llms.openai_llm import OpenAILLM


def test_openai_invoke(monkeypatch):
    class FakeLLM:
        def invoke(self, *args, **kwargs):
            return "fake-response"

    # Mock ChatOpenAI constructor
    monkeypatch.setattr(
        "rag_app.llms.openai_llm.ChatOpenAI",
        lambda model: FakeLLM()
    )

    # ALSO mock API key check
    monkeypatch.setenv("OPENAI_API_KEY", "fake-key")

    user_input = {
        "selected_openai_model": "gpt-test"
    }

    wrapper = OpenAILLM(user_input)
    llm = wrapper.get_llm_model()

    assert llm.invoke("hi") == "fake-response"