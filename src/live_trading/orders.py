from src.live_trading.client import LiveClient


class LiveOrders:

    def __init__(self):

        self.client = LiveClient().get()

    def get_open_orders(self):

        return self.client.get_orders()

    def get_order(self, order_id):

        return self.client.get_order(order_id)

    def cancel(self, order_id):

        return self.client.cancel(order_id)

    def cancel_all(self):

        return self.client.cancel_all()