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
# Utilities
# ─────────────────────────────────────────────────────────────

def apply_theme(theme: str):
    if theme == "Dark":
        st.markdown(
            """
            <style>
            .stApp {
                background-color: #0e1117;
                color: #fafafa;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            """
            <style>
            .stApp {
                background-color: #ffffff;
                color: #262730;
            }
            </style>
            """,
            unsafe_allow_html=True
        )



# ─────────────────────────────────────────────────────────────
# UI Loader
# ─────────────────────────────────────────────────────────────

class BuildSidebar:
    def __init__(self):
        self.config = Config()
        self.user_controls = {}

    def build_sidebar_choices(self):

        st.set_page_config(
            page_title=f"🤖 {self.config.get_page_title()}",
            layout="wide"
        )

        # ─── Theme state ──────────────────────────────────────
        if "theme" not in st.session_state:
            st.session_state.theme = "Light"

        apply_theme(st.session_state.theme)

        # ─── Header ──────────────────────────────────────────
        st.markdown(
            f"""
            <div style="display:flex;align-items:center;gap:20px;margin-bottom:1.5rem;">
                <img src="data:image/png;base64,{IMG_B64}" style="width:120px;" />
                <h1 style="margin:0;">{self.config.get_chat_title()}</h1>
            </div>
            """,
            unsafe_allow_html=True
        )

        # ─── Sidebar ─────────────────────────────────────────
        with st.sidebar:

            self.user_controls["theme"] = st.radio(
                "Theme",
                ["Light", "Dark"],
                horizontal=True,
                index=0 if st.session_state.theme == "Light" else 1
            )

            st.session_state.theme = self.user_controls["theme"]
            apply_theme(st.session_state.theme)

            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()

            self.user_controls["selected_llm"] = st.selectbox(
                "Select LLM",
                llm_options
            )

            if self.user_controls["selected_llm"] == "Groq":
                self.user_controls["selected_groq_model"] = st.selectbox(
                    "Select Model",
                    self.config.get_groq_model_options()
                )

            elif self.user_controls["selected_llm"] == "OpenAI":
                self.user_controls["selected_openai_model"] = st.selectbox(
                    "Select Model",
                    self.config.get_openai_model_options()
                )

            self.user_controls["selected_usecase"] = st.selectbox(
                "Select Usecase",
                usecase_options
            )

        return self.user_controls



if __name__=="__main__":
    obj=BuildSidebar()
    value=obj.build_sidebar_choices()
    print(obj.build_sidebar_choices())
    print(value.get("selected_usecase"))