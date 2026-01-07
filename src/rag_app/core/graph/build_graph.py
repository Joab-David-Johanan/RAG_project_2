from langgraph.graph import StateGraph, START, END
from rag_app.core.schema.build_state import BasicChatbotState
from rag_app.core.nodes.build_node import BuildNodes


class BuildGraph:
    """
    As soon as initialize the Graph class the following should happen,
    1. Model should get loaded
    2. StateGraph should get loaded with the State (the State comes from rag_app/state/) 
    """
    def __init__(self,model):
        self.llm=model
        self.graph_builder=StateGraph(BasicChatbotState)

    def build_basic_chatbot_graph(self):

        self.basic_chatbot_node = BuildNodes(self.llm)

        self.graph_builder.add_node("chatbot", self.basic_chatbot_node.basic_chat)
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_edge("chatbot", END)
    
    def setup_graph(self, usecase:str):

        """
        calls the correct build graph function based on the selected usecase
        """

        if usecase =="Basic Chatbot":
            self.build_basic_chatbot_graph()
        return self.graph_builder.compile()

