"""Main application entry point."""

from contextlib import asynccontextmanager

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.er_data import router as er_data_router
from app.database import init_db
from app.settings import get_settings

load_dotenv()


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
