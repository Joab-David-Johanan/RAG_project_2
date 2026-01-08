from rag_app.llms.route_correct_llm import RouteLLM
from rag_app.core.graph.build_graph import BuildGraph


class GraphController:
    def get_graph(self, user_input: dict):

        # Do not build graph until LLM is selected
        if not user_input.get("selected_llm"):
            return None

        # PASS USER CHOICES INTO ROUTER
        router = RouteLLM(user_input)
        llm = router.get_llm()

        if llm is None:
            return None

        graph_builder = BuildGraph(llm)
        return graph_builder.setup_graph(user_input["selected_usecase"])
