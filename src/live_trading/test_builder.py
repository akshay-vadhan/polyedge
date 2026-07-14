from src.live_trading.order_builder import LiveOrderBuilder


if __name__ == "__main__":

    builder = LiveOrderBuilder()

    print()

    print("=" * 60)

    print("ORDER BUILDER READY")

    print("=" * 60)

    print()

    print(builder.builder)