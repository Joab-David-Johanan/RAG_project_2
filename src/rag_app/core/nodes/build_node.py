from rag_app.core.schema.build_state import BasicChatbotState

class BuildNodes:
    """
    As soon as initialize the Node class the following should happen,
    1. Model should get loaded
    2. The functions in the Node class manipulate the State variables based on LLM response 
       (the State comes from rag_app/state/) 
    """
    def __init__(self, model):
        self.llm=model
    
    def basic_chat(self, state: BasicChatbotState) -> dict:
        ai_msg = self.llm.invoke(state["messages"])
        return {"messages": [ai_msg]}