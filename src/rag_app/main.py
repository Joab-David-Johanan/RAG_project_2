import streamlit as st
from rag_app.ui.build_ui.load_sidebar import BuildSidebar
from rag_app.llms.route_correct_llm import RouteLLM
from rag_app.graph_builder.basic_chatbot_graph import BuildGraph
from rag_app.ui.build_ui.load_conversation import BuildResultDisplay


def load_app():
    # ─── Sidebar (UI always reruns, state persists) ──────────
    ui = BuildSidebar()
    user_input = ui.build_sidebar_choices()

    if not user_input:
        st.error("Failed to load user input")
        return

    # ─── Cache LLM ──────────────────────────────────────────
    if "llm" not in st.session_state:
        with st.spinner("Loading LLM..."):
            router = RouteLLM(user_input)
            st.session_state.llm = router.get_llm()

    # ─── Cache Graph ────────────────────────────────────────
    if "graph" not in st.session_state:
        with st.spinner("Building graph..."):
            graph_builder = BuildGraph(model=st.session_state.llm)
            st.session_state.graph = graph_builder.setup_graph(
                user_input["selected_usecase"]
            )

    # ─── Chat Input ─────────────────────────────────────────
    user_message = st.chat_input("Enter your message")

    if user_message:
        BuildResultDisplay(
            usecase=user_input["selected_usecase"],
            graph=st.session_state.graph,
            user_message=user_message
        ).display()
