import os
from dotenv import load_dotenv

from pydantic import BaseModel
from pydantic_settings import BaseSettings

load_dotenv()


class Config(BaseModel):
    private_key: str | None = os.getenv("PRIVATE_KEY")
    algorithm: str | None = os.getenv("ALGORITHM")


class Settings(BaseSettings):
    config: Config = Config()


settings = Settings()
