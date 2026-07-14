import os
from dotenv import load_dotenv

load_dotenv()

HOST = "https://clob.polymarket.com"

CHAIN_ID = 137

PRIVATE_KEY = os.getenv("PRIVATE_KEY")

WALLET_ADDRESS = os.getenv("WALLET_ADDRESS")

TRADE_SIZE_USD = float(
    os.getenv("TRADE_SIZE_USD", "2")
)

LIVE_TRADING = (
    os.getenv("LIVE_TRADING", "False").lower() == "true"
)