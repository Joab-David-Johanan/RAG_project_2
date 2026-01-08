import base64
import streamlit as st
from pathlib import Path

# choose which type of config file to read from
from rag_app.ui.read_config.read_from_toml import Config
# from rag_app.ui.read_config.read_from_ini import Config


#-------------------
# Paths
#-------------------

PROJECT_ROOT = Path(__file__).resolve().parents[4]
ASSETS_DIR = PROJECT_ROOT / "data" / "assets"
ROBOT_IMG = ASSETS_DIR / "red_transformer.png"


#-------------------
# Utilities
#-------------------

def img_to_base64(path: Path) -> str:
    return base64.b64encode(path.read_bytes()).decode()

IMG_B64 = img_to_base64(ROBOT_IMG)


#-------------------
# Build Pages
#-------------------

class BuildPages:
    def __init__(self):
        self.config = Config()
        self.user_controls = {}

    # Page config can be set only once and should happen before other Streamlit calls
    def init_page(self):
        st.set_page_config(
            page_title=f"{self.config.get_page_title()}",
            layout="wide"
        )

    # Entry point: either show homepage (no usecase yet) or route to selected usecase
    def run(self):
        self.init_page()

        # Decide which usecase to render
        # If the user has not selected a usecase yet, show homepage
        if "selected_usecase" not in st.session_state:
            self.homepage()
            return

        # If a usecase is already selected, route to it
        self.route(st.session_state["selected_usecase"])

    # Router: renders the correct page function based on the chosen usecase
    def route(self, usecase: str):
        self.usecase = usecase

        if usecase == "Basic Chatbot":
            self.basic_chatbot_ui()
        elif usecase == "RAG Chatbot":
            self.rag_chatbot_ui()
        else:
            self.homepage()

        return self.usecase

    #-------------------
    # Homepage
    #-------------------

    def homepage(self):
        # Image and title
        st.markdown(
            f"""
            <div style="display:flex;align-items:center;gap:20px;margin-bottom:1.5rem;">
                <img src="data:image/png;base64,{IMG_B64}" style="width:120px;" />
                <h1>Welcome to the ALL IN ONE RAG APP</h1>
            </div>
            """,
            unsafe_allow_html=True
        )

        # Description line
        st.subheader("What RAG usecase do you want to explore today?")

        usecase_options = self.config.get_usecase_options()

        # Layout buttons in columns for a clean look
        cols = st.columns(len(usecase_options))

        for col, usecase in zip(cols, usecase_options):
            with col:
                if st.button(usecase, use_container_width=True):
                    st.session_state["selected_usecase"] = usecase
                    st.rerun()

    #-------------------
    # Basic Chatbot UI
    #-------------------

    def basic_chatbot_ui(self):

        # Image and chat title
        st.markdown(
            f"""
            <div style="display:flex;align-items:center;gap:20px;margin-bottom:1.5rem;">
                <img src="data:image/png;base64,{IMG_B64}" style="width:120px;" />
                <h1 style="margin:0;">{self.config.get_chat_title()}</h1>
            </div>
            """,
            unsafe_allow_html=True
        )

        # Description line
        st.subheader("Chat directly with a model (no retrieval).")

        # Sidebar: usecase selection + model settings for this page
        with st.sidebar:

            if st.button("Back to Home"):
                st.session_state.pop("selected_usecase", None)
                st.rerun()

            usecase_options = self.config.get_usecase_options()
            self.user_controls["selected_usecase"] = st.selectbox(
                "Select Usecase",
                usecase_options,
                index=usecase_options.index(st.session_state.get("selected_usecase", usecase_options[0]))
            )
            st.session_state["selected_usecase"] = self.user_controls["selected_usecase"]

            llm_options = self.config.get_llm_options()
            self.user_controls["selected_llm"] = st.selectbox("Select LLM", llm_options)

            if self.user_controls["selected_llm"] == "Groq":
                self.user_controls["selected_model"] = st.selectbox(
                    "Select Model",
                    self.config.get_groq_model_options()
                )
            elif self.user_controls["selected_llm"] == "OpenAI":
                self.user_controls["selected_model"] = st.selectbox(
                    "Select Model",
                    self.config.get_openai_model_options()
                )

        # Chat history in session state
        if "messages" not in st.session_state:
            st.session_state["messages"] = []

        # Render previous messages
        for msg in st.session_state["messages"]:
            with st.chat_message(msg["role"]):
                st.write(msg["content"])

        # Chat input
        user_message = st.chat_input("Enter your message")

        if user_message:
            st.session_state["messages"].append({"role": "user", "content": user_message})
            st.session_state["user_message"] = user_message

    #-------------------
    # RAG Chatbot UI
    #-------------------

    def rag_chatbot_ui(self):

        # Page header
        st.markdown(
            f"""
            <div style="display:flex;align-items:center;gap:20px;margin-bottom:1.0rem;">
                <img src="data:image/png;base64,{IMG_B64}" style="width:120px;" />
                <h1 style="margin:0;">RAG Document Search</h1>
            </div>
            """,
            unsafe_allow_html=True
        )

        # Description line
        st.subheader("Ask questions grounded in your documents (retrieval + generation).")

        # Sidebar: usecase selection + RAG settings + model settings for this page
        with st.sidebar:

            if st.button("Back to Home"):
                st.session_state.pop("selected_usecase", None)
                st.rerun()

            uploaded_files = st.file_uploader(
                "Upload your documents",
                type=["pdf", "txt", "md"],
                accept_multiple_files=True
            )

            # Persist uploaded files in session state
            if uploaded_files:
                st.session_state["uploaded_documents"] = uploaded_files

            llm_options = self.config.get_llm_options()
            self.user_controls["selected_llm"] = st.selectbox("Select LLM", llm_options)

            if self.user_controls["selected_llm"] == "Groq":
                self.user_controls["selected_model"] = st.selectbox(
                    "Select Model",
                    self.config.get_groq_model_options()
                )
            elif self.user_controls["selected_llm"] == "OpenAI":
                self.user_controls["selected_model"] = st.selectbox(
                    "Select Model",
                    self.config.get_openai_model_options()
                )

            self.user_controls["top_k"] = st.slider("Top K Documents", 1, 10, 4)
            self.user_controls["chunk_size"] = st.slider("Chunk Size", 256, 2048, 512)

        # Main interaction (you can swap this form to st.chat_input if you want RAG to feel chatty)
        with st.form("search_form"):
            question = st.text_input(
                "Enter your question:",
                placeholder="What would you like to know?"
            )
            submit = st.form_submit_button("Search")

        if submit and question:
            st.session_state["user_message"] = question
            st.write(f"Searching for: {question}")

        return st.session_state.get("user_message")


# Note: This is for local testing only. In your app flow, AppController should call BuildPages().run()
if __name__ == "__main__":
    obj = BuildPages()
    obj.run()
