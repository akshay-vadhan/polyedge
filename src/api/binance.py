import requests

from config import REQUEST_TIMEOUT


class BinanceClient:

    BASE_URL = "https://api.binance.com"

    def get_price(self):

        response = requests.get(

            f"{self.BASE_URL}/api/v3/ticker/price",

            params={

                "symbol": "BTCUSDT"

            },

            timeout=REQUEST_TIMEOUT

        )

        response.raise_for_status()

        return float(

            response.json()["price"]

        )