"""Application settings using pydantic-settings."""

from functools import lru_cache

from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

DEFAULT_DATABASE_URL = "postgresql+psycopg://spei:spei@localhost:5433/spei_intent_guard"


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    # Application settings
    app_name: str = "spei-intent-guard-api"
    debug: bool = False
    host: str = "0.0.0.0"
    port: int = 8000

    # Allowed browser origins for CORS, comma-separated.
    # Empty falls back to the local development origins.
    cors_origin: str = ""

    # Database settings. This is the single source of truth for the database URL:
    # app/database.py and migrations/env.py both read it from here.
    database_url: str = DEFAULT_DATABASE_URL

    @field_validator("database_url")
    @classmethod
    def _require_psycopg_driver(cls, value: str) -> str:
        """Pin Postgres URLs to the installed psycopg driver."""
        if value.startswith("postgresql://"):
            return value.replace("postgresql://", "postgresql+psycopg://", 1)
        return value

    @property
    def cors_origins(self) -> list[str]:
        """Return the allowed browser origins as an explicit list.

        Never returns a wildcard. Starlette answers `allow_origins=["*"]` plus
        `allow_credentials=True` by echoing whichever origin asked, which lets
        any site make credentialed cross-origin calls to this API.
        """
        origins = [origin.strip() for origin in self.cors_origin.split(",") if origin.strip()]
        return origins or ["http://localhost:3000", "http://localhost:3001"]


@lru_cache
def get_settings() -> Settings:
    """Get cached settings instance."""
    return Settings()
