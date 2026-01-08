import base64
import streamlit as st
from pathlib import Path
from rag_app.ui.read_config.read_from_toml import Config


class BasicChatbotPage:
    """
    UI page for the Basic Chatbot usecase.
    """

    def __init__(self):
        self.config = Config()
        self.img_b64 = self._load_logo()

    def _load_logo(self) -> str:
        project_root = Path(__file__).resolve().parents[5]
        img_path = project_root / "data" / "assets" / "red_transformer.png"
        return base64.b64encode(img_path.read_bytes()).decode()

    def render(self):
        """
        Renders the Basic Chatbot UI.
        """

        st.markdown(
            f"""
            <div style="display:flex;align-items:center;gap:20px;margin-bottom:1.5rem;">
                <img src="data:image/png;base64,{self.img_b64}" style="width:120px;" />
                <h1>{self.config.get_chat_title()}</h1>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.subheader("Chat directly with a language model")

        # Sidebar controls
        with st.sidebar:

            if st.button("Back to Home"):
                st.session_state.pop("selected_usecase", None)
                st.rerun()

            st.selectbox(
                "Select LLM",
                self.config.get_llm_options(),
                key="selected_llm"
            )

            if st.session_state["selected_llm"] == "Groq":
                st.selectbox(
                    "Select Model",
                    self.config.get_groq_model_options(),
                    key="selected_model"
                )
            elif st.session_state["selected_llm"] == "OpenAI":
                st.selectbox(
                    "Select Model",
                    self.config.get_openai_model_options(),
                    key="selected_model"
                )

        # Reset chat on model change
        prev_model = st.session_state.get("previous_model")
        curr_model = st.session_state.get("selected_model")

        if prev_model and prev_model != curr_model:
            st.session_state["messages"] = []
            st.session_state.pop("user_message", None)

        st.session_state["previous_model"] = curr_model

        if "messages" not in st.session_state:
            st.session_state["messages"] = []

        for msg in st.session_state["messages"]:
            with st.chat_message(msg["role"]):
                st.write(msg["content"])

        user_message = st.chat_input("Enter your message")

        if user_message:
            st.session_state["messages"].append(
                {"role": "user", "content": user_message}
            )
            st.session_state["user_message"] = user_message
            st.rerun()
