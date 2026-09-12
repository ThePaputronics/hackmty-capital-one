"""Drop and recreate local MVP tables.

Use this only for local synthetic data. Do not point DATABASE_URL at production.
"""

from app.database import engine, init_db
from app.models import Base


def main() -> None:
    """Reset all SQLAlchemy-managed tables."""
    Base.metadata.drop_all(bind=engine)
    init_db()
    print("Local MVP database reset complete.")


if __name__ == "__main__":
    main()
