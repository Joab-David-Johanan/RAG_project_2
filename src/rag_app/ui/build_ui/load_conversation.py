import streamlit as st


class BuildResultDisplay:
    def __init__(self, usecase, graph, user_message):
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message

    def display(self):

        if self.usecase != "Basic Chatbot":
            return

        # Render user message once
        with st.chat_message("user"):
            st.write(self.user_message)

        # Placeholder for assistant streaming
        assistant_container = st.chat_message("assistant")
        assistant_text = ""

        for event in self.graph.stream(
            {"messages": ("user", self.user_message)}
        ):
            for value in event.values():
                msg = value["messages"]
                assistant_text += msg.content
                assistant_container.write(assistant_text)
