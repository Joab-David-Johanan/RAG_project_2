from rag_app.ui.chat.load_conversation import BuildResultDisplay

class OutputController:
    def render(self, user_input: dict, graph):

        if graph is None:
            return  # graph not ready yet

        user_message = user_input.get("user_message")
        if not user_message:
            return

        BuildResultDisplay(
            usecase=user_input["selected_usecase"],
            graph=graph,
            user_message=user_message
        ).display()