import os
import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load environment variables ONCE at startup
load_dotenv()

class OpenAILLM: 
    def __init__(self, user_controls):
        self.user_input = user_controls

    def get_llm_model(self):
        try:
            selected_openai_model = self.user_input["selected_model"]

            if not os.getenv("OPENAI_API_KEY"):
                st.error("Please set the OPENAI_API_KEY")
                st.stop()

            llm = ChatOpenAI(
                model=selected_openai_model
            )

            return llm

        except Exception as e:
            raise RuntimeError(f"Error occurred while loading LLM: {e}")
