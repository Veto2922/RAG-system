from pydantic_settings import BaseSettings
import os
# from dotenv import load_dotenv
# load_dotenv('.env')
class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str
    OPENAI_API_KEY: str
    FILE_ALLOWED_TYPES: list
    FILE_MAX_SIZE: int
    FILE_DEFAULT_CHUNK_SIZE : int
    
    class Config:
        env_file = '.env'

def get_settings():
    # Create Settings instance
    return Settings()

try:
    settings = get_settings()
    print(settings)
except Exception as e:
    print(f"Error creating settings: {e}")
