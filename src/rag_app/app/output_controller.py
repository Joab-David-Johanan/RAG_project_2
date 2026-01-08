from rag_app.ui.build_ui.load_conversation import BuildResultDisplay

class OutputController:
    def render(self, user_input: dict, graph):

        user_message = user_input.get("user_message")

        if not user_message:
            return

        BuildResultDisplay(
            usecase=user_input["selected_usecase"],
            graph=graph,
            user_message=user_message
        ).display()