from rag_app.ui.build_ui.load_sidebar import BuildSidebar


class UIController:
    def get_user_input(self) -> dict:
        ui = BuildSidebar()
        return ui.build_sidebar_choices()