import time

from src.collectors.market_collector import MarketCollector
from src.paper_trading.engine import PaperTradingEngine
from src.paper_trading.trade_manager import TradeManager
from src.utils.logger import logger


class TradingBot:

    def __init__(self):

        self.collector = MarketCollector()

        self.paper = PaperTradingEngine()

        self.manager = TradeManager()

    def run(self):

        logger.success("Bot Started")

        while True:

            try:

                self.collector.collect()

                self.paper.create_trade()

                self.manager.process()

            except Exception as e:

                logger.error(str(e))

            time.sleep(1)


if __name__ == "__main__":

    TradingBot().run()