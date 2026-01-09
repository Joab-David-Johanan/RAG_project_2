import base64
import streamlit as st
from pathlib import Path
from rag_app.ui.read_config.read_from_toml import Config


class HomePage:
    """
    Landing page for the application.
    Responsible only for usecase selection.
    """

    def __init__(self):
        self.config = Config()
        self.img_b64 = self._load_logo()

    def _load_logo(self) -> str:
        """
        Loads and base64-encodes the application logo.
        """
        project_root = Path(__file__).resolve().parents[4]
        img_path = project_root / "data" / "assets" / "red_transformer.png"
        return base64.b64encode(img_path.read_bytes()).decode()

    def _select_usecase(self, usecase: str):
        """
        Callback used by buttons to select a usecase.
        """
        st.session_state["selected_usecase"] = usecase

    def render(self):
        """
        Renders the homepage UI.
        """

        st.markdown(
            f"""
            <div style="display:flex;align-items:center;gap:20px;margin-bottom:1.5rem;">
                <img src="data:image/png;base64,{self.img_b64}" style="width:120px;" />
                <h1>Welcome to the ALL IN ONE RAG APP</h1>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.subheader("Choose a usecase to get started")

        usecases = self.config.get_usecase_options()
        cols = st.columns(len(usecases))

        for col, usecase in zip(cols, usecases):
            with col:
                st.button(
                    usecase,
                    use_container_width=True,
                    on_click=self._select_usecase,
                    args=(usecase,),
                    key=f"home_{usecase}",
                )
