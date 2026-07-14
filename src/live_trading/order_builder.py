from py_clob_client.order_builder.builder import OrderBuilder

from src.live_trading.client import LiveClient


class LiveOrderBuilder:

    def __init__(self):

        client = LiveClient().get()

        self.client = client

        self.builder = client.builder

    def build_buy_yes(

        self,

        token_id,

        price,

        size

    ):

        return self.builder.create_order(

            token_id=token_id,

            price=price,

            size=size,

            side="BUY"

        )

    def build_buy_no(

        self,

        token_id,

        price,

        size

    ):

        return self.builder.create_order(

            token_id=token_id,

            price=price,

            size=size,

            side="BUY"

        )

    def build_sell(

        self,

        token_id,

        price,

        size

    ):

        return self.builder.create_order(

            token_id=token_id,

            price=price,

            size=size,

            side="SELL"

        )