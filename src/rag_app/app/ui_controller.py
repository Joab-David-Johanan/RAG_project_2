import streamlit as st
from rag_app.ui.router import UIRouter


class UIController:
    def get_user_input(self) -> dict:
        ui = UIRouter()

        # Render the UI (homepage or selected usecase)
        ui.run()

        # Read user input from Streamlit session state
        return {
            "selected_usecase": st.session_state.get("selected_usecase"),
            "selected_llm": st.session_state.get("selected_llm"),
            "selected_model": st.session_state.get("selected_model"),
            "user_message": st.session_state.get("user_message"),
            "top_k": st.session_state.get("top_k"),
            "chunk_size": st.session_state.get("chunk_size"),
        }   