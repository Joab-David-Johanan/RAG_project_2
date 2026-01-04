import pytest
from rag_app.core.nodes.basic_chatbot_node import BasicChatbotNode


class DummyModel:
    def invoke(self, messages):
        return f"invoked: {messages}"

def test_basic_node_process():
    node = BasicChatbotNode(DummyModel())
    state = {"messages": ["hi"]}
    result = node.process(state)
    assert isinstance(result, dict)
    assert "messages" in result
    assert result["messages"] == "invoked: ['hi']"
