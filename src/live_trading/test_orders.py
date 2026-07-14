from src.live_trading.orders import LiveOrders


if __name__ == "__main__":

    orders = LiveOrders()

    print()

    print("=" * 60)

    print("OPEN ORDERS")

    print("=" * 60)

    print()

    try:

        data = orders.get_open_orders()

        print(data)

    except Exception as e:

        print("ERROR")

        print(e)