import time
import traceback
from src.database.database import Database
from src.database.repository import Repository
from src.collectors.market_collector import MarketCollector
from src.paper_trading.engine import PaperTradingEngine
from src.paper_trading.trade_manager import TradeManager
from src.utils.logger import logger
from src.live_trading.live_engine import LiveTradeEngine
from src.live_trading.config import LIVE_TRADING

class TradingBot:

    def __init__(self):

        self.collector = MarketCollector()

        self.paper = PaperTradingEngine()

        self.manager = TradeManager()

        self.db = Database()

        self.repo = Repository(self.db)

        self.live = LiveTradeEngine()

    def run(self):

        logger.success("=" * 60)
        logger.success("POLYMARKET EDGE BOT STARTED")
        logger.success("=" * 60)

        cycle = 0

        try:

            while True:

                cycle += 1

                logger.info(f"Cycle #{cycle}")

                start = time.time()

                try:

                    tick = self.collector.collect()

                    if tick is None:

                        time.sleep(1)

                        continue

                    # ---------------------------------
                    # Save Tick
                    # ---------------------------------

                    self.repo.insert_market_tick(tick)

                    logger.success("Tick Saved")

                    # ---------------------------------
                    # Generate Signal
                    # ---------------------------------

                    trade = self.paper.create_trade()

                    if trade:

                        logger.success(

                            f"New Trade : {trade['side']} @ {trade['entry_price']}"

                        )

                    if trade and LIVE_TRADING:

                        logger.info(

                            "Sending trade to Live Engine"

                        )

                        self.live.execute_signal(

                            self.collector.market,

                            trade["side"]

                        )

                    # ---------------------------------
                    # Manage Trades
                    # ---------------------------------

                    self.manager.process()

                except Exception:

                    logger.error(traceback.format_exc())

                    logger.info("Bot recovered")

                logger.info(

                    f"Cycle Time : {round(time.time()-start,2)} sec"

                )

                time.sleep(1)

        except KeyboardInterrupt:

            logger.success("=" * 60)
            logger.success("BOT STOPPED")
            logger.success("=" * 60)


if __name__ == "__main__":

    TradingBot().run()