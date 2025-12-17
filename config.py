from pydantic_settings import BaseSettings, SettingsConfigDict



class Settings(BaseSettings):
    private_key: str  | None  = None
    algorithm: str | None = None
    expire: float | None  = None 
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding= "utf-8"
    )

settings = Settings()
