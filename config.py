from pydantic import BaseModel
from pydantic_settings import BaseSettings


class Config(BaseModel):
    private_key: str = "my_app_key"
    algoritm: str = "HS256"


class Settings(BaseSettings):
    config: Config = Config()


settings = Settings()
