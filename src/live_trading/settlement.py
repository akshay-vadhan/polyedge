import json
import sqlite3

from config import POLYMARKET_API

from src.api.gamma import GammaClient
from src.utils.logger import logger


class SettlementEngine:

    def __init__(self):

        self.gamma = GammaClient()

        self.db = "data/polymarket.db"

    def _connect(self):

        return sqlite3.connect(self.db)

    def get_winner(self, slug):

        event = self.gamma.get_event_by_slug(slug)

        market = event["markets"][0]

        if not market["closed"]:

            return None

        prices = json.loads(
            market["outcomePrices"]
        )

        yes = float(prices[0])
        no = float(prices[1])

        if yes == 1:

            return "YES"

        if no == 1:

            return "NO"

        return None

    def settle_trade(self, order_id):

        conn = self._connect()

        conn.row_factory = sqlite3.Row

        cur = conn.cursor()

        cur.execute("""

            SELECT *

            FROM live_trades

            WHERE order_id=?

        """,

        (order_id,))

        trade = cur.fetchone()

        if trade is None:

            logger.warning(
                "Trade Not Found"
            )

            conn.close()

            return False

        trade = dict(trade)

        winner = self.get_winner(

            trade["market_slug"]

        )

        if winner is None:

            logger.info(

                "Market Not Resolved Yet"

            )

            conn.close()

            return False

        pnl = trade["usd_amount"]

        if trade["side"] != winner:

            pnl = -trade["usd_amount"]

        roi = (

            pnl /

            trade["usd_amount"]

        ) * 100

        cur.execute("""

            UPDATE live_trades

            SET

            status=?,

            pnl=?,

            roi=?,

            closed_at=datetime('now')

            WHERE order_id=?

        """,

        (

            "CLOSED",

            pnl,

            roi,

            order_id

        ))

        conn.commit()

        conn.close()

        logger.success(

            f"Trade Settled | Winner={winner} | PnL={pnl}"

        )

        return True