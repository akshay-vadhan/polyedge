from py_clob_client.clob_types import (
    OrderArgs,
    CreateOrderOptions
)

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

        size,

        tick_size,

        neg_risk

    ):

        order = OrderArgs(

            token_id=token_id,

            price=price,

            size=size,

            side="BUY"

        )

        options = CreateOrderOptions(

            tick_size=tick_size,

            neg_risk=neg_risk

        )

        return self.builder.create_order(

            order,

            options

        )

    def build_buy_no(

        self,

        token_id,

        price,

        size,

        tick_size,

        neg_risk

    ):

        order = OrderArgs(

            token_id=token_id,

            price=price,

            size=size,

            side="BUY"

        )

        options = CreateOrderOptions(

            tick_size=tick_size,

            neg_risk=neg_risk

        )

        return self.builder.create_order(

            order,

            options

        )

    def build_sell(

        self,

        token_id,

        price,

        size,

        tick_size,

        neg_risk

    ):

        order = OrderArgs(

            token_id=token_id,

            price=price,

            size=size,

            side="SELL"

        )

        options = CreateOrderOptions(

            tick_size=tick_size,

            neg_risk=neg_risk

        )

        return self.builder.create_order(

            order,

            options

        )