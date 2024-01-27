import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv
from typing import List
import json

load_dotenv()


class Settings(BaseSettings):
    API_VERSION: str = "v1"
    API_V1_STR: str = f"/api/{API_VERSION}"

    DB_HOST: str = os.getenv("DB_HOST")
    DB_PORT: str = os.getenv("DB_PORT")
    DB_NAME: str = os.getenv("DB_NAME")
    DB_PASS: str = os.getenv("DB_PASS")
    DB_USER: str = os.getenv("DB_USER")

    API_KEY: str = os.getenv("API_KEY")

    ASYNC_DATABASE_URI: str = (
        f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )