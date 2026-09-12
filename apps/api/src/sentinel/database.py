"""Database engine, session management, and Base definition."""

from collections.abc import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from sentinel.config import get_settings


class Base(DeclarativeBase):
    """SQLAlchemy Declarative Base class."""


def get_engine(db_url: str | None = None):
    """Create SQLAlchemy engine with appropriate dialect arguments."""
    settings = get_settings()
    url = db_url or settings.database_url
    connect_args = {}
    if url.startswith("sqlite"):
        connect_args["check_same_thread"] = False
    return create_engine(url, pool_pre_ping=True, connect_args=connect_args)


settings = get_settings()
engine = get_engine()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator[Session, None, None]:
    """Provide a transactional database session per request."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
