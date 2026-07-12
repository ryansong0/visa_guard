from pydantic_settings import BaseSettings
from pydantic import HttpUrl

class Settings(BaseSettings):
    APP_NAME: str = "VisaGuard Compliance Engine"
    VERSION: str = "2.0"
    OLLAMA_URL: str = "http://127.0.0.1:11434"
    LLM_MODEL: str = "llama3.2:latest"
    EMBEDDING_MODEL: str = "sentence-transformers/all-MiniLM-L6-v2"
    VECTOR_THRESHOLD: float = 0.42

    class Config:
        env_file = ".env"

settings = Settings()