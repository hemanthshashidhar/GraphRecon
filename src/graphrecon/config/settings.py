from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Global project settings.
    """

    browser_headless: bool = Field(default=True)

    timeout: int = Field(default=30000)

    max_depth: int = Field(default=3)

    max_pages: int = Field(default=100)

    model_config = SettingsConfigDict(
        env_prefix="GRAPHRECON_",
        env_file=".env",
        extra="ignore",
    )


settings = Settings()
