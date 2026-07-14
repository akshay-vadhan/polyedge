from src.market.manager import MarketManager
from src.live_trading.executor import LiveExecutor


if __name__ == "__main__":

    market = MarketManager().get_market()

    executor = LiveExecutor()

    signed = executor.create_signed_order(

        market=market,

        side="YES",

        usd_amount=2

    )

    print()

    print("=" * 60)

    print("SIGNED ORDER")

    print("=" * 60)

    print()

    print(signed)