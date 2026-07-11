import requests
import json
from config import REQUEST_TIMEOUT
from src.api.models import OrderBook, PriceLevel


class ClobClient:

    BASE_URL = "https://clob.polymarket.com"

    def __init__(self):
        self.session = requests.Session()

    def _get(self, endpoint, params=None):

        response = self.session.get(
            f"{self.BASE_URL}{endpoint}",
            params=params,
            timeout=REQUEST_TIMEOUT
        )

        response.raise_for_status()

        data = response.json()

        #print("\n================ RAW RESPONSE ================\n")
        #print(json.dumps(data, indent=2))
        #print("\n==============================================\n")

        return data

    # -----------------------------------------------------

    def get_orderbook(self, token_id):

        data = self._get(
            "/book",
            {"token_id": token_id}
        )

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

        mid = (best_bid + best_ask) / 2 if bids and asks else 0

        bid_volume = sum(x.size for x in bids)

        ask_volume = sum(x.size for x in asks)

        imbalance = 0

        if bid_volume + ask_volume > 0:

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


    # -----------------------------------------------------

    def get_best_bid(self, token_id):

        return self.get_orderbook(token_id).best_bid

    def get_best_ask(self, token_id):

        return self.get_orderbook(token_id).best_ask

    def get_mid_price(self, token_id):

        return self.get_orderbook(token_id).mid_price

    def get_spread(self, token_id):

        return self.get_orderbook(token_id).spread

    def get_orderbook_imbalance(self, token_id):

        return self.get_orderbook(token_id).imbalance

    # -----------------------------------------------------
