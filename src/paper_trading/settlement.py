import requests

from config import POLYMARKET_API


class SettlementEngine:

    def winner(self, market_slug):

        response = requests.get(

            f"{POLYMARKET_API}/events",

            params={

                "slug": market_slug

            }

        )

        event = response.json()[0]

        market = event["markets"][0]

        if not market["closed"]:

            return None

        prices = market["outcomePrices"]

        if isinstance(prices, str):

            import json

            prices = json.loads(prices)

        yes = float(prices[0])

        no = float(prices[1])

        if yes > no:

            return "YES"

        return "NO"