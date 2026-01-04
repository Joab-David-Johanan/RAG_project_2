from typing_extensions import TypedDict, List
from langgraph.graph.message import add_messages
from typing import Annotated

class BasicChatbotState(TypedDict):
    """
    Create the state that is to be used in the basic chatbot graph builder
    """

    # add_messages is a reducer that appends the message to the list, does not overwrite the messages
    messages:Annotated[List,add_messages]
    