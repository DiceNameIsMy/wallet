from pydantic import BaseSettings


class Settings(BaseSettings):
    api_token: str = ""

    class Config(BaseSettings.Config):
        env_prefix = "TG_"
        env_file = ".env"
