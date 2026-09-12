"""Shared pytest configuration.

Point DATABASE_URL at a throwaway SQLite file before anything imports the app.
`app.database` builds its engine at import time and the FastAPI lifespan calls
`init_db()` against that engine, so without this the test suite tries to reach
the Postgres in compose.db.yaml and fails when it is not running.
"""

import os
import tempfile
from pathlib import Path

_TEST_DB = Path(tempfile.gettempdir()) / "spei-intent-guard-test.db"
_TEST_DB.unlink(missing_ok=True)

# Must happen before `app.settings` is first instantiated.
os.environ["DATABASE_URL"] = f"sqlite:///{_TEST_DB}"
