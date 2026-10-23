from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    app_name: str = "Doctobot API"
    database_url: str = "sqlite:///./doctobot.db"


settings = Settings()
