import streamlit as st
from rag_app.ui.build_ui.load_conversation import BuildResultDisplay


class OutputController:
    def render(self, user_input: dict, graph):
        user_message = st.chat_input("Enter your message")

        if user_message:
            BuildResultDisplay(
                usecase=user_input["selected_usecase"],
                graph=graph,
                user_message=user_message
            ).display()