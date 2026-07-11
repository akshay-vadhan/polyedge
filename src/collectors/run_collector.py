import signal
import sys
import time

from src.collectors.market_collector import MarketCollector
from src.database.database import Database
from src.database.repository import Repository
from src.utils.logger import logger


class CollectorService:

    def __init__(self):

        self.running = True

        self.collector = MarketCollector()

        self.db = Database()

        self.repo = Repository(self.db)

        signal.signal(signal.SIGINT, self.stop)
        signal.signal(signal.SIGTERM, self.stop)

    def stop(self, signum, frame):

        logger.warning("Stopping Collector...")

        self.running = False

        self.db.close()

        sys.exit(0)

    def run(self):

        logger.success("Collector Started")

        while self.running:

            try:

                tick = self.collector.collect()

                self.repo.insert_market_tick(tick)

                logger.info(
                    f"{tick['market_slug']} | "
                    f"BTC {tick['btc_price']:.2f} | "
                    f"YES {tick['yes_price']:.3f} | "
                    f"NO {tick['no_price']:.3f} | "
                    f"Last {tick['last_trade']:.2f} | "
                    f"Spread {tick['spread']:.2f}"
                )

                time.sleep(1)

            except Exception as e:

                logger.error(e)

                time.sleep(5)


if __name__ == "__main__":

    CollectorService().run()