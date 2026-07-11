"""
Polymarket CLOB API Client
"""

from __future__ import annotations

import requests

from config import REQUEST_TIMEOUT
from src.utils.logger import logger


class ClobClient:

    BASE_URL = "https://clob.polymarket.com"

    def __init__(self):
        self.session = requests.Session()

    def get_orderbook(self, token_id: str):

        url = f"{self.BASE_URL}/book"

        params = {
            "token_id": token_id
        }

        try:

            response = self.session.get(
                url,
                params=params,
                timeout=REQUEST_TIMEOUT
            )

            response.raise_for_status()

            return response.json()

        except requests.RequestException as e:

            logger.error(f"CLOB Error : {e}")

            return None

    def get_best_bid_ask(self, token_id: str):

        book = self.get_orderbook(token_id)

        if not book:
            return None

        bids = book.get("bids", [])
        asks = book.get("asks", [])

        best_bid = bids[0] if bids else None
        best_ask = asks[0] if asks else None

        return {
            "bid": best_bid,
            "ask": best_ask
        }