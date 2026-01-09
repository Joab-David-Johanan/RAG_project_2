from langgraph.graph import StateGraph, START, END
from rag_app.core.schema.build_state import BasicChatbotState
from rag_app.core.nodes.build_node import BuildNodes


class BuildGraph:
    def __init__(self, model):
        self.llm = model
        self.graph_builder = StateGraph(BasicChatbotState)

    def build_basic_chatbot_graph(self):
        node = BuildNodes(self.llm)

        self.graph_builder.add_node("chatbot", node.basic_chat)

        # Explicit entrypoint
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_edge("chatbot", END)

    def setup_graph(self, usecase: str):
        """
        Builds and compiles the graph for the selected usecase.
        """

        if usecase == "Basic Chatbot":
            self.build_basic_chatbot_graph()
        else:

            self.build_basic_chatbot_graph()
            # raise ValueError(
            #     f"No graph defined for usecase: {usecase}"
            # )

        return self.graph_builder.compile()
