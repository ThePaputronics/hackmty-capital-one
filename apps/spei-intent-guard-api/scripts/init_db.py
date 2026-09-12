"""Create database tables for the local SPEI Intent Guard MVP database."""

from sqlalchemy import inspect

from app.database import engine, init_db


def main() -> None:
    """Create all SQLAlchemy tables and print the resulting table names."""
    init_db()
    table_names = sorted(inspect(engine).get_table_names())
    print("Database tables ready:")
    for table_name in table_names:
        print(f"- {table_name}")


if __name__ == "__main__":
    main()
