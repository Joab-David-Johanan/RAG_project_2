import os
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load environment variables ONCE at startup
load_dotenv()


class GroqLLM:
    def __init__(self, user_controls):
        self.user_input = user_controls

    def get_llm_model(self):
        try:
            selected_groq_model = self.user_input["selected_model"]

            # Validate API key
            if not os.getenv("GROQ_API_KEY"):
                st.error("Please set the GROQ_API_KEY in your environment or .env file")
                st.stop()

            llm = ChatGroq(
                model=selected_groq_model
            )

            return llm

        except Exception as e:
            raise RuntimeError(f"Error occurred while initializing Groq LLM: {e}")
