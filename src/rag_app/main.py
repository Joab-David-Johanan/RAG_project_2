import streamlit as st
from rag_app.ui.build_ui.load_ui import LoadStreamlitUI

def load_app():
    """
    Loads and runs the app using the load_ui.py file which contains the class
    that provides the sidebar and usercontrols for the app
    """

    # creates the object of the LoadStreamlitUI class, 
    # which initializes the Config class the reads from the .ini config file
    ui=LoadStreamlitUI()
    # returns the selected user control values
    user_input=ui.load_streamlit_ui()

    if not user_input:
        st.error("Error: Failed to load user input from the UI")
        return  
    
    # creating user chat box
    user_message=st.chat_input("Enter you message: ")