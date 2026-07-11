import json
import requests

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

        return response.json()

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

                closed=market["closed"],

                enable_orderbook=market["enableOrderBook"]

            )

        raise MarketNotFound(
            "No Active BTC Market Found."
        )