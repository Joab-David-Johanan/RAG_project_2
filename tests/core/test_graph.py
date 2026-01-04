from rag_app.core.graph.basic_chatbot_graph import BuildGraph

class DummyModel:
    pass

def test_graph_node_names():
    gb = BuildGraph(model=DummyModel())
    graph = gb.setup_graph(usecase="Basic Chatbot")
    assert graph is not None
