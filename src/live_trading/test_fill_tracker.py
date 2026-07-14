from src.live_trading.fill_tracker import FillTracker


if __name__ == "__main__":

    tracker = FillTracker()

    order_id = "PUT_REAL_ORDER_ID_HERE"

    order = tracker.wait_until_finished(

        order_id

    )

    print()

    print("=" * 60)

    print(order)

    print("=" * 60)