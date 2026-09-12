"""FastAPI server exposing /sim/status and running the bank-player in background."""

import argparse
import logging
import os
import threading
from contextlib import asynccontextmanager
from typing import Any
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from generator.player import BankPlayer, SimulationStatus

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")
logger = logging.getLogger("generator-server")

API_URL = os.environ.get("API_URL", "http://localhost:8000")
SPEED = float(os.environ.get("SIM_SPEED", "6.0"))
AUTO_START = os.environ.get("AUTO_START", "false").lower() in ("true", "1", "yes")
API_KEY = os.environ.get("API_KEY") or None

player = BankPlayer(api_base_url=API_URL, speed_seconds_per_day=SPEED, api_key=API_KEY)
sim_thread: threading.Thread | None = None


def run_simulation_worker():
    """Execute warmup and active streaming in background thread."""
    try:
        logger.info("Starting simulation worker (warmup + 30-day stream)...")
        player.run_warmup()
        player.play_active_stream()
        logger.info("Simulation worker finished.")
    except Exception as exc:
        logger.exception("Simulation worker encountered an error: %s", exc)
        player.status.state = f"error: {exc}"


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Optionally auto-start simulation on service startup."""
    global sim_thread
    if AUTO_START:
        sim_thread = threading.Thread(target=run_simulation_worker, daemon=True)
        sim_thread.start()
    yield


app = FastAPI(title="Sentinel Simulation Status Service", lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/sim/status")
def get_simulation_status() -> dict[str, Any]:
    """Return live status of the simulation clock, counters, and ground-truth metrics."""
    from dataclasses import asdict
    return asdict(player.status)


@app.post("/sim/start")
def start_simulation() -> dict[str, str]:
    """Trigger the bank-player simulation stream."""
    global sim_thread, player
    if player.status.state in ("warming_up", "streaming"):
        return {"status": "already_running", "state": player.status.state}

    # Reset player for fresh run
    player = BankPlayer(api_base_url=API_URL, speed_seconds_per_day=SPEED, api_key=API_KEY)
    sim_thread = threading.Thread(target=run_simulation_worker, daemon=True)
    sim_thread.start()
    return {"status": "started", "state": "warming_up"}


def main():
    """CLI entry point for generator service."""
    parser = argparse.ArgumentParser(description="Sentinel Bank Player Simulation Service")
    parser.add_argument("--api-url", default=API_URL, help="Target Sentinel API base URL")
    parser.add_argument("--speed", type=float, default=SPEED, help="Seconds per simulated day (6.0 for demo, 0 for max speed)")
    parser.add_argument("--port", type=int, default=8001, help="Service port (default 8001)")
    parser.add_argument("--host", default="0.0.0.0", help="Service host")
    parser.add_argument("--run-now", action="store_true", help="Start simulation immediately without waiting for /sim/start")

    args = parser.parse_args()
    global player, sim_thread
    player = BankPlayer(api_base_url=args.api_url, speed_seconds_per_day=args.speed, api_key=API_KEY)

    if args.run_now:
        sim_thread = threading.Thread(target=run_simulation_worker, daemon=True)
        sim_thread.start()

    uvicorn.run(app, host=args.host, port=args.port)


if __name__ == "__main__":
    main()
