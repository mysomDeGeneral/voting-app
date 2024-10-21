import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str 

    class Config:
        env_file = os.path.join(os.path.dirname(__file__), '.env')

settings = Settings()
    