from src.live_trading.client import LiveClient
from src.live_trading.account import LiveAccount
from src.live_trading.order_builder import LiveOrderBuilder
from src.api.exceptions import (
    InsufficientBalanceError,
    MarketClosedError
)


class LiveExecutor:

    def __init__(self):

        self.client = LiveClient().get()

        self.account = LiveAccount()

        self.builder = LiveOrderBuilder()

    def calculate_shares(

        self,

        usd_amount,

        price,

        min_size

    ):

        shares = usd_amount / price

        if shares < min_size:

            shares = min_size

        return round(shares, 4)

    def validate(

        self,

        market,

        usd_amount

    ):

        print()

        print("=" * 60)

        print("VALIDATION")

        print("=" * 60)

        print()

        if not market.accepting_orders:

            logger.error(
                f"Market Closed: {market.slug}"
            )

            raise MarketClosedError(
                f"Market '{market.slug}' is not accepting orders."
            )

        balance = float(
            self.account.get_balance()["balance"]
        )

        logger.info(f"Wallet Balance : {balance}")

        if balance < usd_amount:

            logger.error(
                f"Insufficient Balance | Have={balance} | Need={usd_amount}"
            )

            raise InsufficientBalanceError(
                f"Balance={balance}, Required={usd_amount}"
            )

        logger.success("Validation Passed")

    def create_signed_order(

        self,

        market,

        side,

        usd_amount

    ):

        self.validate(

            market,

            usd_amount

        )

        if side.upper() == "YES":

            token = market.up_token

            price = market.yes_price

        else:

            token = market.down_token

            price = market.no_price

        shares = self.calculate_shares(

            usd_amount,

            price,

            market.min_order_size

        )

        print()

        print("Price :", price)

        print("Shares :", shares)

        print()

        signed = self.builder.build(

            token_id=token,

            side="BUY",

            price=price,

            size=shares,

            tick_size=market.tick_size,

            neg_risk=market.neg_risk

        )

        return signed