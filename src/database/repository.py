from src.database.queries import INSERT_MARKET_TICK

from src.database.queries import INSERT_PAPER_TRADE

class Repository:

    def __init__(self, db):
        self.db = db

    def insert_market_tick(self, tick):

        self.db.execute(

            INSERT_MARKET_TICK,

            (

                tick["timestamp"],
                tick["market_slug"],

                tick["btc_price"],

                tick["yes_price"],
                tick["no_price"],

                tick["yes_bid"],
                tick["yes_ask"],
                tick["yes_mid"],
                tick["yes_spread"],

                tick["yes_bid_volume"],
                tick["yes_ask_volume"],
                tick["yes_imbalance"],

                tick["no_bid"],
                tick["no_ask"],
                tick["no_mid"],
                tick["no_spread"],

                tick["no_bid_volume"],
                tick["no_ask_volume"],
                tick["no_imbalance"],

                tick["last_trade"],

                tick["liquidity"],

                tick["volume"],

                tick["one_hour_change"]

            )

        )

    def insert_trade(self, trade):

        self.db.execute(

            INSERT_PAPER_TRADE,

            (

                trade["trade_id"],

                trade["market_slug"],

                trade["side"],

                trade["status"],

                trade["entry_time"],

                trade["exit_time"],

                trade["entry_price"],

                trade["exit_price"],

                trade["btc_entry"],

                trade["btc_exit"],

                trade["confidence"],

                trade["score"],

                trade["pnl"],

                trade["roi"],

                trade["result"],

                trade["reason"]

            )

        )

    def get_open_trades(self):

        return self.db.fetchall(

            """

            SELECT *

            FROM paper_trades

            WHERE status='OPEN'

            """

        )


    def close_trade(

        self,

        trade_id,

        exit_time,

        exit_price,

        btc_exit,

        pnl,

        roi,

        result

    ):

        self.db.execute(

            """

            UPDATE paper_trades

            SET

                status='CLOSED',

                exit_time=?,

                exit_price=?,

                btc_exit=?,

                pnl=?,

                roi=?,

                result=?

            WHERE trade_id=?

            """,

            (

                exit_time,

                exit_price,

                btc_exit,

                pnl,

                roi,

                result,

                trade_id

            )

        )


    def trade_exists(self, market_slug):

        row = self.db.fetchone(

            """

            SELECT COUNT(*)

            FROM paper_trades

            WHERE market_slug=?

            """,

            (market_slug,)

        )

        return row[0] > 0