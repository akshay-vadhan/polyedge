import time
from datetime import datetime, timezone

from src.api.gamma import GammaClient
from src.utils.logger import logger


class MarketManager:

    def __init__(self):

        self.gamma = GammaClient()

        self.current_market = None
        self.current_bucket = None

    def _current_bucket(self):

        now = int(
            datetime.now(
                timezone.utc
            ).timestamp()
        )

        return (now // 300) * 300

    def _load_market(self):

        last_error = None

        for attempt in range(1, 6):

            try:

                market = self.gamma.find_active_btc_market()

                logger.success(
                    f"Active Market : {market.slug}"
                )

                return market

            except Exception as e:

                last_error = e

                logger.warning(
                    f"Gamma retry {attempt}/5 : {e}"
                )

                time.sleep(2)

        raise last_error

    def get_market(self):

        bucket = self._current_bucket()

        # Same 5-minute bucket
        if (
            self.current_market is not None
            and bucket == self.current_bucket
        ):
            return self.current_market

        logger.info(
            f"Loading BTC Market ({bucket})..."
        )

        market = self._load_market()

        self.current_market = market
        self.current_bucket = bucket

        return market