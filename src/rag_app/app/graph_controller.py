import streamlit as st
from rag_app.llms.route_correct_llm import RouteLLM
from rag_app.core.graph.build_graph import BuildGraph


class GraphController:
    def get_graph(self, user_input: dict):
        # Cache LLM
        if "llm" not in st.session_state:
            router = RouteLLM(user_input)
            st.session_state.llm = router.get_llm()

        # Cache Graph
        if "graph" not in st.session_state:
            builder = BuildGraph(model=st.session_state.llm)
            st.session_state.graph = builder.setup_graph(
                user_input["selected_usecase"]
            )

        return st.session_state.graph