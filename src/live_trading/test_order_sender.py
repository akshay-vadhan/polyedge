from src.market.manager import MarketManager
from src.live_trading.executor import LiveExecutor
from src.live_trading.order_sender import OrderSender


def main():

    market = MarketManager().get_market()

    executor = LiveExecutor()

    sender = OrderSender()

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

    # Uncomment ONLY after funding wallet
    #
    # response = sender.send(signed)
    #
    # print(response)


if __name__ == "__main__":

    main()