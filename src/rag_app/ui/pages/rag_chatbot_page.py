import base64
import streamlit as st
from pathlib import Path
from rag_app.ui.read_config.read_from_toml import Config


class RagChatbotPage:
    """
    UI page for the RAG Chatbot usecase.
    """

    def __init__(self):
        self.config = Config()
        self.img_b64 = self._load_logo()

    def _load_logo(self) -> str:
        project_root = Path(__file__).resolve().parents[4]
        img_path = project_root / "data" / "assets" / "red_transformer.png"
        return base64.b64encode(img_path.read_bytes()).decode()

    def render(self):
        """
        Renders the RAG Chatbot UI.
        """

        st.markdown(
            f"""
            <div style="display:flex;align-items:center;gap:20px;margin-bottom:1.0rem;">
                <img src="data:image/png;base64,{self.img_b64}" style="width:120px;" />
                <h1>RAG Document Search</h1>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.subheader("Upload documents and ask grounded questions")

        with st.sidebar:

            if st.button("Back to Home"):
                st.session_state.pop("selected_usecase", None)
                st.rerun()

            st.file_uploader(
                "Upload documents",
                type=["pdf", "txt", "md"],
                accept_multiple_files=True,
                key="uploaded_documents"
            )

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

            st.slider("Top K Documents", 1, 10, 4, key="top_k")
            st.slider("Chunk Size", 256, 2048, 512, key="chunk_size")

        question = st.chat_input("Ask a question about your documents")

        if question:
            st.session_state["user_message"] = question
            st.write(f"Searching for: {question}")
