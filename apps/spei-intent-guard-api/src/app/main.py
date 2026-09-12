"""Main application entry point."""

import logging
from contextlib import asynccontextmanager

from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError

from app.api.er_data import router as er_data_router
from app.database import init_db
from app.settings import get_settings

load_dotenv()

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Initialize database tables on startup for the MVP."""
    init_db()
    yield


settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    description="SPEI Intent Guard MVP API",
    version="0.1.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


@app.exception_handler(IntegrityError)
async def integrity_error_handler(request: Request, exc: IntegrityError) -> JSONResponse:
    """Return 409 instead of 500 when a write violates a database constraint.

    Duplicate external IDs and references to rows that do not exist are client
    mistakes, not server faults. The underlying error is logged in full so the
    cause is still visible in the server logs.
    """
    logger.warning("integrity error on %s %s: %s", request.method, request.url.path, exc.orig)
    return JSONResponse(
        status_code=409,
        content={
            "detail": (
                "The request conflicts with an existing record or references one that does "
                "not exist."
            )
        },
    )


app.include_router(er_data_router)


@app.get("/health")
async def health():
    """Health check endpoint."""
    return {"status": "healthy", "service": settings.app_name}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app.main:app",
        host=settings.host,
        port=settings.port,
        reload=True,
    )
