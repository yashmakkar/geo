from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

_ = load_dotenv()

class Settings(BaseSettings):
    openai_api_key: str
    google_api_key: str
    huggingface_api_key: str
    user_agent: str
    qdrant_url: str

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="allow")

config = Settings()