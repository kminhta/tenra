from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    PROJECT_NAME: str = "Tenra"
    DATABASE_URL: str
    API_SECRET_KEY: str
    API_PORT: int = 8000
    CORS_ORIGINS: List[str] = ["http://localhost:3000"]
    
    model_config = {
        "env_file": "../.env",
        "extra": "ignore"
    }

settings = Settings()
