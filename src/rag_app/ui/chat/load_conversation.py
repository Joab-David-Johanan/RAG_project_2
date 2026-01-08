import streamlit as st

class BuildResultDisplay:
    def __init__(self, usecase, graph, user_message):
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message

    def display(self):

        if self.graph is None:
            return

        if self.usecase != "Basic Chatbot":
            return

        assistant_text = ""

        for event in self.graph.stream(
            {"messages": ("user", self.user_message)}
        ):
            for value in event.values():
                msgs = value.get("messages")
                if not msgs:
                    continue

                if isinstance(msgs, list):
                    for m in msgs:
                        assistant_text += m.content
                else:
                    assistant_text += msgs.content

        # Append assistant response ONCE
        st.session_state["messages"].append(
            {"role": "assistant", "content": assistant_text}
        )

        # 🔥 CRITICAL: clear transient trigger
        st.session_state.pop("user_message", None)

        # Rerun to render updated history
        st.rerun()

