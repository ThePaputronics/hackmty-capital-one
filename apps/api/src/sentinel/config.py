"""Application configuration and settings."""

from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Runtime configuration loaded from environment variables."""

    app_name: str = "Sentinel SPEI Guard API"
    environment: str = "development"
    debug: bool = False
    host: str = "0.0.0.0"
    port: int = 8000

    # Database settings
    database_url: str = "postgresql+psycopg://sentinel:sentinel@localhost:5432/sentinel_db"

    # API Security and CORS
    api_key_required: bool = False
    institution_api_key: str = "sentinel-dev-secret-key"
    cors_origins: list[str] = ["*"]

    # Ruleset and model versions
    ruleset_version: str = "2026.09-sentinel-v1"

    # Default MTU cap in MXN (1,500 UDIs ≈ $12,800 MXN)
    mtu_cap_mxn: float = 12800.0

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    """Return cached application settings singleton."""
    return Settings()
