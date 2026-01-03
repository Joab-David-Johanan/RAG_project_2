from pathlib import Path
import tomllib
from rag_app.ui.config.config_schema import AppConfig

PROJECT_ROOT = Path(__file__).resolve().parents[4]
CONFIG_FILE = PROJECT_ROOT / "src" /"rag_app" / "ui" / "config" / "uiconfig.toml"


class Config:
    def __init__(self, config_file: Path = CONFIG_FILE):
        with open(config_file, "rb") as f:
            raw_config = tomllib.load(f)

        self.config = AppConfig(**raw_config)

    def get_page_title(self) -> str:
        return self.config.ui.page_title

    def get_chat_title(self) -> str:
        return self.config.ui.chat_title

    def get_llm_options(self) -> list[str]:
        return self.config.ui.options.llm_options

    def get_usecase_options(self) -> list[str]:
        return self.config.ui.options.usecase_options

    def get_groq_model_options(self) -> list[str]:
        return self.config.models.groq_model_options

    def get_openai_model_options(self) -> list[str]:
        return self.config.models.openai_model_options

if __name__=='__main__':
    obj=Config()
    print(obj.get_groq_model_options())
    print(obj.get_usecase_options())