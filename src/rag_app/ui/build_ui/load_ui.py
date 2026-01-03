import base64
import streamlit as st
from pathlib import Path
#from rag_app.ui.read_config.read_from_ini import Config
from rag_app.ui.read_config.read_from_toml import Config


# ─────────────────────────────────────────────────────────────
# Paths
# ─────────────────────────────────────────────────────────────

PROJECT_ROOT = Path(__file__).resolve().parents[4]
ASSETS_DIR = PROJECT_ROOT / "data" / "assets"
ROBOT_IMG = ASSETS_DIR / "red_transformer.png"


# ─────────────────────────────────────────────────────────────
# Utilities
# ─────────────────────────────────────────────────────────────

def img_to_base64(path: Path) -> str:
    return base64.b64encode(path.read_bytes()).decode()


IMG_B64 = img_to_base64(ROBOT_IMG)


# ─────────────────────────────────────────────────────────────
# UI Loader
# ─────────────────────────────────────────────────────────────

class LoadStreamlitUI:
    def __init__(self):
        """
        Initializes UI config and user control state.
        """
        self.config = Config()
        self.user_controls = {}

    def load_streamlit_ui(self):

        # ─── Page Config ──────────────────────────────────────
        st.set_page_config(
            page_title=f"🤖 {self.config.get_page_title()}",
            layout="wide"
        )

        # ─── Header (Image + Title, perfectly centered) ───────
        st.markdown(
            f"""
            <div style="
                display: flex;
                align-items: center;
                gap: 20px;
                margin-bottom: 1.5rem;
            ">
                <img 
                    src="data:image/png;base64,{IMG_B64}" 
                    style="width: 120px;"
                />
                <h1 style="margin: 0;">
                    {self.config.get_chat_title()}
                </h1>
            </div>
            """,
            unsafe_allow_html=True
        )

        # ─── Sidebar ──────────────────────────────────────────
        with st.sidebar:

            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()

            # LLM selection
            self.user_controls["selected_llm"] = st.selectbox(
                "Select LLM",
                llm_options
            )

            if self.user_controls["selected_llm"] == "Groq":
                groq_model_options = self.config.get_groq_model_options()
                self.user_controls["selected_model"] = st.selectbox(
                    "Select Model",
                    groq_model_options
                )

                self.user_controls["GROQ_API_KEY"] = (
                    st.session_state.setdefault("GROQ_API_KEY", "")
                )
                self.user_controls["GROQ_API_KEY"] = st.text_input(
                    "API Key",
                    type="password",
                    value=self.user_controls["GROQ_API_KEY"]
                )

                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning(
                        "Please enter your GROQ API key to proceed.\n"
                        "Get one at: https://console.groq.com/keys"
                    )

            elif self.user_controls["selected_llm"] == "OpenAI":
                openai_model_options = self.config.get_openai_model_options()
                self.user_controls["selected_model"] = st.selectbox(
                    "Select Model",
                    openai_model_options
                )

                self.user_controls["OPENAI_API_KEY"] = (
                    st.session_state.setdefault("OPENAI_API_KEY", "")
                )
                self.user_controls["OPENAI_API_KEY"] = st.text_input(
                    "API Key",
                    type="password",
                    value=self.user_controls["OPENAI_API_KEY"]
                )

                if not self.user_controls["OPENAI_API_KEY"]:
                    st.warning(
                        "Please enter your OpenAI API key to proceed.\n"
                        "Get one at: https://platform.openai.com/api-keys"
                    )

            # Usecase selection
            self.user_controls["selected_usecase"] = st.selectbox(
                "Select Usecase",
                usecase_options
            )

        return self.user_controls


if __name__=="__main__":
    obj=LoadStreamlitUI()
    print(obj.load_streamlit_ui())