import streamlit as st
from rag_app.app.ui_controller import UIController
from rag_app.app.graph_controller import GraphController
from rag_app.app.output_controller import OutputController


class AppController:
    def __init__(self):
        self.ui_controller = UIController()
        self.graph_controller = GraphController()
        self.output_controller = OutputController()

    def run(self):
        user_input = self.ui_controller.get_user_input()
        if not user_input:
            return

        usecase = user_input.get("selected_usecase")
        if not usecase:
            return

        graph = self.graph_controller.get_graph(user_input)
        if graph is None:
            return

        self.output_controller.render(user_input, graph)
