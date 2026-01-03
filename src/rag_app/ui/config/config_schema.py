from pydantic import BaseModel
from typing import List


# ─────────────────────────────────────────────────────────────
# UI Options
# ─────────────────────────────────────────────────────────────

class UIOptions(BaseModel):
    llm_options: List[str]
    usecase_options: List[str]


# ─────────────────────────────────────────────────────────────
# UI Config
# ─────────────────────────────────────────────────────────────

class UIConfig(BaseModel):
    page_title: str
    chat_title: str
    options: UIOptions


# ─────────────────────────────────────────────────────────────
# Model Config
# ─────────────────────────────────────────────────────────────

class ModelConfig(BaseModel):
    groq_model_options: List[str]
    openai_model_options: List[str]


# ─────────────────────────────────────────────────────────────
# App Config (Root)
# ─────────────────────────────────────────────────────────────

class AppConfig(BaseModel):
    ui: UIConfig
    models: ModelConfig
