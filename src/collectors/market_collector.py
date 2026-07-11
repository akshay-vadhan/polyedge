from datetime import datetime, timezone

from src.api.gamma import GammaClient
from src.api.clob import ClobClient
from src.market.manager import MarketManager

from src.api.binance import BinanceClient

class MarketCollector:

    def __init__(self):

        self.manager = MarketManager()

        self.clob = ClobClient()

        self.binance = BinanceClient()

    def collect(self):

        market = self.manager.get_market()

        btc_price = self.binance.get_price()

        yes_book = self.clob.get_orderbook(
            market.up_token
        )

        no_book = self.clob.get_orderbook(
            market.down_token
        )

        return {

            "timestamp": datetime.now(
                timezone.utc
            ).isoformat(),

            "market_slug": market.slug,

            "btc_price": btc_price,

            # Gamma
            "yes_price": market.yes_price,
            "no_price": market.no_price,

            "last_trade": market.last_trade,
            "liquidity": market.liquidity,
            "volume": market.volume,
            "one_hour_change": market.one_hour_change,

            # YES Book
            "yes_bid": yes_book.best_bid,
            "yes_ask": yes_book.best_ask,
            "yes_mid": yes_book.mid_price,
            "yes_spread": yes_book.spread,

            "yes_bid_volume": yes_book.bid_volume,
            "yes_ask_volume": yes_book.ask_volume,
            "yes_imbalance": yes_book.imbalance,

            # NO Book
            "no_bid": no_book.best_bid,
            "no_ask": no_book.best_ask,
            "no_mid": no_book.mid_price,
            "no_spread": no_book.spread,

            "no_bid_volume": no_book.bid_volume,
            "no_ask_volume": no_book.ask_volume,
            "no_imbalance": no_book.imbalance
        }