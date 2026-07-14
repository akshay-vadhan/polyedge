from src.market.manager import MarketManager

from src.live_trading.live_engine import (
    LiveTradeEngine
)


if __name__ == "__main__":

    market = MarketManager().get_market()

    engine = LiveTradeEngine()

    result = engine.execute_signal(

        market,

        "YES"

    )

    print()

    print(result)