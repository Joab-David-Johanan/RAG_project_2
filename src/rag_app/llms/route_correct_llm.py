from rag_app.llms.groq_llm import GroqLLM
from rag_app.llms.openai_llm import OpenAILLM


class RouteLLM:
    """
    Routes user choice to the correct LLM based on sidebar selection
    """

    def __init__(self, user_choices: dict):
        self.user_choices = user_choices

    def get_llm(self):
        selected_llm = self.user_choices.get("selected_llm")

        if selected_llm == "Groq":
            return GroqLLM(self.user_choices).get_llm_model()

        if selected_llm == "OpenAI":
            return OpenAILLM(self.user_choices).get_llm_model()

        raise ValueError(f"Unsupported LLM selection: {selected_llm}")
