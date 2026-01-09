import streamlit as st
from rag_app.ui.read_config.read_from_toml import Config
from rag_app.ui.pages.homepage import HomePage
from rag_app.ui.pages.basic_chatbot_page import BasicChatbotPage
from rag_app.ui.pages.rag_chatbot_page import RagChatbotPage


class UIRouter:
    """
    Central router that decides which page to render.
    This file contains no UI logic other than routing.
    """

    def __init__(self):
        self.config = Config()

    def init_page(self):
        """
        Streamlit page configuration.
        Must be called exactly once before any UI rendering.
        """
        st.set_page_config(page_title=self.config.get_page_title(), layout="wide")

    def run(self):
        """
        Application entry point for UI rendering.
        """
        self.init_page()

        selected_usecase = st.session_state.get("selected_usecase")

        if not selected_usecase:
            HomePage().render()
            return

        if selected_usecase == "Basic Chatbot":
            BasicChatbotPage().render()
        elif selected_usecase == "RAG Chatbot":
            RagChatbotPage().render()
        else:
            HomePage().render()
