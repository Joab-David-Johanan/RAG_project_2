from rag_app.state.basic_chatbot_state import BasicChatbotState

class BasicChatbotNode:
    """
    As soon as initialize the Node class the following should happen,
    1. Model should get loaded
    2. The functions in the Node class manipulate the State variables based on LLM response 
       (the State comes from rag_app/state/) 
    """
    def __init__(self, model):
        self.llm=model
    
    def process(self,state:BasicChatbotState)->dict:
        """
        Process the input state and generate a chat response
        """
        return {"messages":self.llm.invoke(state["messages"])}