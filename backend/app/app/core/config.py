import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv
from typing import List
import json
from loguru import logger
import sys
from pathlib import Path


class Settings(BaseSettings):

    API_VERSION: str = "v1"
    API_V1_STR: str = f"/api/{API_VERSION}"

    DB_HOST: str
    DB_PORT: str
    DB_NAME: str
    DB_PASS: str
    DB_USER: str

    @property
    def DATABASE_URI(self) -> str:
        return f"postgresql://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    @property
    def ASYNC_DATABASE_URI(self) -> str:
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    # github module settings
    GITHUB_ACCESS_TOKEN: str

    LOCATION: str
    MAX_USERS: int
    MAX_REPOS_PER_USER: int
    model_config = SettingsConfigDict(case_sensitive=True, env_file=".env")


class LogConfig:
    LOGGING_LEVEL = "DEBUG"
    LOGGING_FORMAT = "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"

    @staticmethod
    def configure_logging():
        logger.remove()

        logger.add(
            sys.stderr, format=LogConfig.LOGGING_FORMAT, level=LogConfig.LOGGING_LEVEL
        )


LogConfig.configure_logging()

settings = Settings()