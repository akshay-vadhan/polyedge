from src.live_trading.config import LIVE_TRADING

from src.live_trading.risk import RiskManager
from src.live_trading.executor import LiveExecutor
from src.live_trading.order_sender import OrderSender
from src.live_trading.fill_tracker import FillTracker
from src.live_trading.trade_logger import TradeLogger
from src.live_trading.geoblock import GeoBlockChecker
from src.utils.logger import logger
from src.api.exceptions import (
    InsufficientBalanceError,
    RiskLimitExceeded,
    DuplicatePositionError,
    MarketClosedError
)


class LiveTradeEngine:

    def __init__(self):

        self.risk = RiskManager()

        self.executor = LiveExecutor()

        self.sender = OrderSender()

        self.tracker = FillTracker()

        self.logger = TradeLogger()

        self.geo = GeoBlockChecker()

    def execute_signal(

        self,

        market,

        side

    ):

        logger.info(

            f"Executing Live Signal : {side}"

        )


        geo = self.geo.check()

        if geo:

            print()

            print("=" * 60)

            print("GEOBLOCK")

            print("=" * 60)

            print(f"Blocked : {geo.get('blocked')}")
            print(f"Country : {geo.get('country')}")
            print(f"Region  : {geo.get('region')}")
            print(f"IP      : {geo.get('ip')}")

            print()

            if geo.get("blocked"):

                logger.error(

                    f"Trading blocked ({geo.get('country')})"

                )

                return None
        # ---------------------------------

        # Risk

        # ---------------------------------

        try:

            self.risk.validate(

                market.slug,

                side

            )

        except (

            InsufficientBalanceError,

            RiskLimitExceeded,

            DuplicatePositionError,

            MarketClosedError

        ) as e:

            logger.error(str(e))

            return None

        usd_amount = self.risk.get_trade_amount()

        # ---------------------------------

        # Build

        # ---------------------------------

        signed = self.executor.create_signed_order(

            market=market,

            side=side,

            usd_amount=usd_amount

        )

        # ---------------------------------

        # Safety

        # ---------------------------------

        if not LIVE_TRADING:

            logger.warning(

                "LIVE_TRADING=False"

            )

            logger.warning(

                "Order NOT submitted."

            )

            return signed

        # ---------------------------------

        # Submit

        # ---------------------------------

        response = self.sender.send(

            signed

        )

        order_id = response["orderID"]

        # ---------------------------------

        # Track

        # ---------------------------------

        order = self.tracker.wait_until_finished(

            order_id

        )

        # ---------------------------------

        # Log

        # ---------------------------------

        self.logger.log_open_trade(

            order_id=order_id,

            market_slug=market.slug,

            token_id=(

                market.up_token

                if side == "YES"

                else market.down_token

            ),

            side=side,

            shares=order.get(

                "originalSize",

                0

            ),

            price=order.get(

                "price",

                0

            ),

            usd_amount=usd_amount

        )

        return order