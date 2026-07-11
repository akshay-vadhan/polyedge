from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

# -----------------------------
# Paths
# -----------------------------

BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"
LOG_DIR = BASE_DIR / "logs"
REPORT_DIR = BASE_DIR / "reports"

DATABASE_PATH = DATA_DIR / "polymarket.db"

# -----------------------------
# API
# -----------------------------

POLYMARKET_API = "https://gamma-api.polymarket.com"

BINANCE_API = "https://api.binance.com"

# -----------------------------
# General
# -----------------------------

POLL_INTERVAL = 1

ORDERBOOK_DEPTH = 20

REQUEST_TIMEOUT = 10

MAX_RETRIES = 3

# -----------------------------
# Environment
# -----------------------------

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "")