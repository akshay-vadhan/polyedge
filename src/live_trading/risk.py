import sqlite3
from src.utils.logger import logger
from src.live_trading.account import LiveAccount
from src.api.exceptions import (
    RiskLimitExceeded,
    DuplicatePositionError,
    InsufficientBalanceError
)

from src.live_trading.config import (
    TRADE_SIZE_USD,
    MAX_OPEN_TRADES,
    MAX_DAILY_LOSS,
    MIN_BALANCE
)


class RiskManager:

    def __init__(self):

        self.db = "data/polymarket.db"

        self.account = LiveAccount()

        # Config

        self.trade_size = TRADE_SIZE_USD

        self.max_open_trades = MAX_OPEN_TRADES

        self.max_daily_loss = MAX_DAILY_LOSS

        self.min_balance = MIN_BALANCE

    def _connect(self):

        return sqlite3.connect(self.db)

    def wallet_balance(self):

        return float(

            self.account.get_balance()["balance"]

        )

    def open_positions(self):

        conn = self._connect()

        cur = conn.cursor()

        cur.execute("""

            SELECT COUNT(*)

            FROM live_trades

            WHERE status='OPEN'

        """)

        count = cur.fetchone()[0]

        conn.close()

        return count

    def daily_pnl(self):

        conn = self._connect()

        cur = conn.cursor()

        cur.execute("""

            SELECT

            COALESCE(SUM(pnl),0)

            FROM live_trades

            WHERE status='CLOSED'

        """)

        pnl = cur.fetchone()[0]

        conn.close()

        return pnl

    def duplicate_position(

        self,

        market_slug,

        side

    ):

        conn = self._connect()

        cur = conn.cursor()

        cur.execute("""

            SELECT COUNT(*)

            FROM live_trades

            WHERE

            market_slug=?

            AND side=?

            AND status='OPEN'

        """,

        (

            market_slug,

            side

        ))

        count = cur.fetchone()[0]

        conn.close()

        return count > 0
        
    def get_trade_amount(self):

        return self.trade_size


    def validate(

        self,

        market_slug,

        side

    ):

        balance = self.wallet_balance()

        if balance < self.min_balance:

            logger.error(
                f"Risk Check Failed | Balance={balance}"
            )

            raise InsufficientBalanceError(

                f"Wallet Balance = {balance}"

            )

        if self.open_positions() >= self.max_open_trades:

            logger.error(
                "Risk Check Failed | Max Open Trades"
            )

            raise RiskLimitExceeded(

                "Maximum Open Trades Reached."

            )

        if self.daily_pnl() <= -self.max_daily_loss:

            logger.error(
                "Risk Check Failed | Daily Loss"
            )

            raise RiskLimitExceeded(

                "Daily Loss Limit Hit."

            )

        if self.duplicate_position(

            market_slug,

            side

        ):
            logger.warning(
                f"Duplicate Position | {market_slug} | {side}"
            )

            raise DuplicatePositionError(

                f"{side} already open."

            )

        logger.success("Risk Validation Passed")

        return True