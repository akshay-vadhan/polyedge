import sqlite3
from datetime import datetime, timezone

from src.utils.logger import logger


class TradeLogger:

    def __init__(self):

        self.db = "data/polymarket.db"

    def _connect(self):

        return sqlite3.connect(self.db)

    def log_open_trade(

        self,

        order_id,

        market_slug,

        token_id,

        side,

        shares,

        price,

        usd_amount

    ):

        conn = self._connect()

        cur = conn.cursor()

        cur.execute(
            """
            INSERT INTO live_trades (

                order_id,

                market_slug,

                token_id,

                side,

                shares,

                entry_price,

                usd_amount,

                status,

                created_at

            )

            VALUES (?,?,?,?,?,?,?,?,?)

            """,

            (

                order_id,

                market_slug,

                token_id,

                side,

                shares,

                price,

                usd_amount,

                "OPEN",

                datetime.now(
                    timezone.utc
                ).isoformat()

            )

        )

        conn.commit()

        conn.close()

        logger.success(
            f"Trade Logged : {order_id}"
        )

    def log_fill(

        self,

        order_id,

        fill_price

    ):

        conn = self._connect()

        cur = conn.cursor()

        cur.execute(

            """

            UPDATE live_trades

            SET

                status=?,

                fill_price=?,

                filled_at=?

            WHERE

                order_id=?

            """,

            (

                "FILLED",

                fill_price,

                datetime.now(
                    timezone.utc
                ).isoformat(),

                order_id

            )

        )

        conn.commit()

        conn.close()

    def close_trade(

        self,

        order_id,

        exit_price,

        pnl

    ):

        conn = self._connect()

        cur = conn.cursor()

        cur.execute(

            """

            UPDATE live_trades

            SET

                status=?,

                exit_price=?,

                pnl=?,

                closed_at=?

            WHERE

                order_id=?

            """,

            (

                "CLOSED",

                exit_price,

                pnl,

                datetime.now(
                    timezone.utc
                ).isoformat(),

                order_id

            )

        )

        conn.commit()

        conn.close()