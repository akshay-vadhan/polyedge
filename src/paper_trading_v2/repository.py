"""
Repository Layer
"""

from src.paper_trading_v2.database import Database


class Repository:

    def __init__(self):

        self.db = Database()

    # --------------------------

    def save_position(self, position):

        self.db.execute(

            """

            INSERT INTO positions(

                position_id,

                market_slug,

                side,

                entry_price,

                shares,

                trade_amount,

                current_price,

                current_value,

                unrealized_pnl,

                max_payout,

                max_profit,

                max_loss,

                status

            )

            VALUES(

                ?,?,?,?,?,?,?,?,?,?,?,?,?

            )

            """,

            (

                position.position_id,

                position.market_slug,

                position.side,

                position.entry_price,

                position.shares,

                position.trade_amount,

                position.current_price,

                position.current_value,

                position.unrealized_pnl,

                position.max_payout,

                position.max_profit,

                position.max_loss,

                position.status

            )

        )

    # --------------------------

    def get_open_position(self):

        return self.db.fetchone(

            """

            SELECT *

            FROM positions

            WHERE status='OPEN'

            LIMIT 1

            """

        )

    # --------------------------

    def close_position(

        self,

        position_id,

        exit_price,

        payout,

        pnl,

        roi,

        result

    ):

        self.db.execute(

            """

            UPDATE positions

            SET

                status='CLOSED',

                current_price=?,

                current_value=?,

                unrealized_pnl=?,

                result=?

            WHERE position_id=?

            """,

            (

                exit_price,

                payout,

                pnl,

                result,

                position_id

            )

        )