from configparser import ConfigParser

class Config:
    def __init__(self, config_file=r'src\rag_app\ui\uiconfig.ini'):
        """
        Docstring for __init__
        
        When the object of the class is created, the ui config file is automatically read.

        :param self: Description
        :param config_file: contains relative path of the ui config file
        """
        self.config=ConfigParser()
        self.config.read(config_file)
    
    def get_llm_options(self):
        """
        Docstring for get_llm_options
        
        We use the ["DEFAULT"] and ["LLM_OPTIONS"] keys in the config file
        to get the values and we split on ", " (comma and space).

        :param self: Description
        """
        return self.config["DEFAULT"].get("LLM_OPTIONS").split(", ")
    
    def get_usecase_options(self):
        """
        Docstring for get_usecase_options
        
        We use the ["DEFAULT"] and ["USECASE_OPTIONS"] keys in the config file
        to get the values and we split on ", " (comma and space).

        :param self: Description
        """
        return self.config["DEFAULT"].get("USECASE_OPTIONS").split(", ")
    
    def get_groq_model_options(self):
        """
        Docstring for get_groq_model_options
        
        We use the ["DEFAULT"] and ["GROQ_MODEL_OPTIONS"] keys in the config file
        to get the values and we split on ", " (comma and space).

        :param self: Description
        """
        return self.config["DEFAULT"].get("GROQ_MODEL_OPTIONS").split(", ")
    
    def get_openai_model_options(self):
        """
        Docstring for get_openai_model_options
        
        We use the ["DEFAULT"] and ["OPENAI_MODEL_OPTIONS"] keys in the config file
        to get the values and we split on ", " (comma and space).

        :param self: Description
        """
        return self.config["DEFAULT"].get("OPENAI_MODEL_OPTIONS").split(", ")
    
    def get_page_title(self):
        return self.config["DEFAULT"].get("PAGE_TITLE")
    
    def get_chat_title(self):
        return self.config["DEFAULT"].get("CHAT_TITLE")
    