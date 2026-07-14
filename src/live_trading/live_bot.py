import time

from src.collectors.market_collector import MarketCollector
from src.live_trading.live_engine import LiveTradeEngine

from src.utils.logger import logger


class LiveBot:

    def __init__(self):

        self.collector = MarketCollector()

        self.engine = LiveTradeEngine()

    def generate_signal(self, snapshot):

        """
        Temporary Signal.

        Later this will call the real
        SignalEngine.
        """

        return None

    def run(self):

        logger.success(
            "LIVE BOT STARTED"
        )

        while True:

            try:

                snapshot = self.collector.collect()

                if snapshot is None:

                    time.sleep(1)

                    continue

                signal = self.generate_signal(
                    snapshot
                )

                if signal is not None:

                    logger.info(

                        f"Signal : {signal}"

                    )

                    self.engine.execute_signal(

                        self.collector.market,

                        signal

                    )

                time.sleep(1)

            except KeyboardInterrupt:

                logger.warning(

                    "Live Bot Stopped"

                )

                break

            except Exception as e:

                logger.exception(e)

                time.sleep(2)