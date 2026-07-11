import requests

from config import REQUEST_TIMEOUT
from src.api.models import OrderBook, PriceLevel
from src.utils.logger import logger


class ClobClient:

    BASE_URL = "https://clob.polymarket.com"

    def __init__(self):

        self.session = requests.Session()

    def get_orderbook(self, token_id):

        url = f"{self.BASE_URL}/book"

        response = self.session.get(
            url,
            params={
                "token_id": token_id
            },
            timeout=REQUEST_TIMEOUT
        )

        response.raise_for_status()

        data = response.json()

        bids = [
            PriceLevel(
                float(x["price"]),
                float(x["size"])
            )
            for x in data.get("bids", [])
        ]

        asks = [
            PriceLevel(
                float(x["price"]),
                float(x["size"])
            )
            for x in data.get("asks", [])
        ]

        best_bid = bids[0].price if bids else 0

        best_ask = asks[0].price if asks else 0

        spread = best_ask - best_bid

        mid = (
            (best_bid + best_ask) / 2
            if best_bid and best_ask
            else 0
        )

        bid_volume = sum(x.size for x in bids)

        ask_volume = sum(x.size for x in asks)

        imbalance = 0

        if (bid_volume + ask_volume) > 0:

            imbalance = (
                bid_volume - ask_volume
            ) / (
                bid_volume + ask_volume
            )

        return OrderBook(

            token_id=token_id,

            best_bid=best_bid,

            best_ask=best_ask,

            mid_price=mid,

            spread=spread,

            bid_volume=bid_volume,

            ask_volume=ask_volume,

            imbalance=imbalance,

            bids=bids,

            asks=asks

        )