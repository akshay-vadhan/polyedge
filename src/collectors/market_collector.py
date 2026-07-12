from datetime import datetime, timezone
import time

from src.market.manager import MarketManager
from src.api.clob import ClobClient
from src.api.binance import BinanceClient

from src.utils.logger import logger


class MarketCollector:

    def __init__(self):

        self.manager = MarketManager()

        self.clob = ClobClient()

        self.binance = BinanceClient()

        # cache
        self.market = None
        self.yes_book = None
        self.no_book = None

        self.last_market_update = 0
        self.last_orderbook_update = 0

    def collect(self):

        now = time.time()

        # ------------------------------------
        # Refresh Gamma every 30 sec
        # ------------------------------------

        if (
            self.market is None
            or now - self.last_market_update >= 30
        ):

            self.market = self.manager.get_market()

            self.last_market_update = now

        # ------------------------------------
        # Refresh Orderbook every 2 sec
        # ------------------------------------

        if (
            self.yes_book is None
            or now - self.last_orderbook_update >= 2
        ):

            try:

                self.yes_book = self.clob.get_orderbook(
                    self.market.up_token
                )

                self.no_book = self.clob.get_orderbook(
                    self.market.down_token
                )

                self.last_orderbook_update = now

            except Exception as e:

                logger.warning(
                    f"Orderbook Error : {e}"
                )

                return None

        # ------------------------------------
        # BTC every second
        # ------------------------------------

        btc_price = self.binance.get_price()

        return {

            "timestamp": datetime.now(
                timezone.utc
            ).isoformat(),

            "market_slug": self.market.slug,

            "btc_price": btc_price,

            "yes_price": self.market.yes_price,
            "no_price": self.market.no_price,

            "last_trade": self.market.last_trade,
            "liquidity": self.market.liquidity,
            "volume": self.market.volume,
            "one_hour_change": self.market.one_hour_change,

            "yes_bid": self.yes_book.best_bid,
            "yes_ask": self.yes_book.best_ask,
            "yes_mid": self.yes_book.mid_price,
            "yes_spread": self.yes_book.spread,

            "yes_bid_volume": self.yes_book.bid_volume,
            "yes_ask_volume": self.yes_book.ask_volume,
            "yes_imbalance": self.yes_book.imbalance,

            "no_bid": self.no_book.best_bid,
            "no_ask": self.no_book.best_ask,
            "no_mid": self.no_book.mid_price,
            "no_spread": self.no_book.spread,

            "no_bid_volume": self.no_book.bid_volume,
            "no_ask_volume": self.no_book.ask_volume,
            "no_imbalance": self.no_book.imbalance

        }