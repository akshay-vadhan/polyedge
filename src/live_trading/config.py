import os
from dotenv import load_dotenv

load_dotenv()

# ==========================================================
# Polymarket
# ==========================================================

HOST = "https://clob.polymarket.com"

CHAIN_ID = 137

PRIVATE_KEY = os.getenv("PRIVATE_KEY")

WALLET_ADDRESS = os.getenv("WALLET_ADDRESS")

FUNDER_ADDRESS = os.getenv("FUNDER_ADDRESS")

SIGNATURE_TYPE = int(
    os.getenv("SIGNATURE_TYPE", "0")
)

LIVE_TRADING = (
    os.getenv("LIVE_TRADING", "False").lower() == "true"
)

# ==========================================================
# Trading
# ==========================================================

TRADE_SIZE_USD = float(
    os.getenv("TRADE_SIZE_USD", "2")
)

MAX_OPEN_TRADES = int(
    os.getenv("MAX_OPEN_TRADES", "1")
)

MAX_DAILY_LOSS = float(
    os.getenv("MAX_DAILY_LOSS", "10")
)

MIN_BALANCE = float(
    os.getenv("MIN_BALANCE", "10")
)

# ==========================================================
# Orders
# ==========================================================

DEFAULT_ORDER_TYPE = "GTC"

POST_ONLY = False

ORDER_TIMEOUT = 30

POLL_INTERVAL = 1