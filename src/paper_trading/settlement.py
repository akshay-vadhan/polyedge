import json
import requests

from config import POLYMARKET_API


class SettlementEngine:

    def winner(self, market_slug):

        try:

            response = requests.get(
                f"{POLYMARKET_API}/events",
                params={"slug": market_slug},
                timeout=10
            )

            response.raise_for_status()

            events = response.json()

            if not events:
                return None

            event = events[0]

            if not event.get("markets"):
                return None

            market = event["markets"][0]

            if not market.get("closed", False):
                return None

            prices = market["outcomePrices"]

            if isinstance(prices, str):
                prices = json.loads(prices)

            yes = float(prices[0])
            no = float(prices[1])

            if yes > no:
                return "YES"

            return "NO"

        except Exception:

            return None