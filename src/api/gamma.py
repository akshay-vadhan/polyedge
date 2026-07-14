import requests
import json
from datetime import datetime, timezone

from config import POLYMARKET_API, REQUEST_TIMEOUT
from src.utils.logger import logger
from src.api.models import Market
from src.api.exceptions import GammaAPIError, MarketNotFound


class GammaClient:

    def __init__(self):

        self.base_url = POLYMARKET_API

    def _bucket_timestamps(self):

        now = int(datetime.now(timezone.utc).timestamp())

        current = (now // 300) * 300

        previous = current - 300

        future = current + 300

        return [
            current,
            previous,
            future
        ]

    def _request(self, slug):

        response = requests.get(
            f"{self.base_url}/events",
            params={"slug": slug},
            timeout=REQUEST_TIMEOUT
        )

        response.raise_for_status()

        data = response.json()

        return data

    def get_event_by_slug(self, slug):

        logger.info(f"Fetching {slug}")

        try:
            events = self._request(slug)

        except requests.RequestException as e:
            raise GammaAPIError(str(e))

        if not events:
            raise MarketNotFound(f"{slug} not found.")

        return events[0]

    def find_active_btc_market(self):

        for ts in self._bucket_timestamps():

            slug = f"btc-updown-5m-{ts}"

            logger.info(f"Searching {slug}")

            try:

                events = self._request(slug)

            except requests.RequestException as e:

                raise GammaAPIError(str(e))

            if not events:

                continue

            event = events[0]

            if len(event["markets"]) == 0:

                continue

            market = event["markets"][0]



            print("\n========== RAW GAMMA MARKET ==========\n")
            print(json.dumps(market, indent=2))
            print("\n======================================\n")

            if market["closed"]:

                continue

            tokens = json.loads(
                market["clobTokenIds"]
            )

            logger.success(
                f"Found {slug}"
            )

            return Market(

                slug=slug,

                condition_id=market["conditionId"],

                up_token=tokens[0],

                down_token=tokens[1],

                # NEW
                tick_size=str(market["orderPriceMinTickSize"]),

                neg_risk=market["negRisk"],

                min_order_size=float(market["orderMinSize"]),

                end_time=market["endDate"],

                accepting_orders=market["acceptingOrders"],

                closed=market["closed"],

                enable_orderbook=market["enableOrderBook"],

                yes_price=float(
                    json.loads(
                        market["outcomePrices"]
                    )[0]
                ),

                no_price=float(
                    json.loads(
                        market["outcomePrices"]
                    )[1]
                ),

                best_bid=float(
                    market.get("bestBid", 0)
                ),

                best_ask=float(
                    market.get("bestAsk", 0)
                ),

                last_trade=float(
                    market.get("lastTradePrice", 0)
                ),

                spread=float(
                    market.get("spread", 0)
                ),

                liquidity=float(
                    market.get("liquidity", 0)
                ),

                volume=float(
                    market.get("volume", 0)
                ),

                one_hour_change=float(
                    market.get("oneHourPriceChange", 0)
                )

            )

        raise MarketNotFound(
            "No Active BTC Market Found."
        )