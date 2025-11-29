from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    PROJECT_NAME: str = "Tenra"
    DATABASE_URL: str
    API_SECRET_KEY: str
    API_PORT: int = 8000
    CORS_ORIGINS: List[str] = ["http://localhost:3000"]
    
    class Config:
        env_file = "../.env"

settings = Settings()
