import sqlite3


class PositionManager:

    def __init__(self):

        self.db = "data/polymarket.db"

    def _connect(self):

        return sqlite3.connect(self.db)

    def get_open_positions(self):

        conn = self._connect()

        conn.row_factory = sqlite3.Row

        cur = conn.cursor()

        cur.execute("""

            SELECT *

            FROM live_trades

            WHERE status='OPEN'

            ORDER BY created_at DESC

        """)

        rows = cur.fetchall()

        conn.close()

        return [dict(r) for r in rows]

    def get_position(

        self,

        market_slug

    ):

        conn = self._connect()

        conn.row_factory = sqlite3.Row

        cur = conn.cursor()

        cur.execute("""

            SELECT *

            FROM live_trades

            WHERE

            market_slug=?

            AND status='OPEN'

            LIMIT 1

        """,

        (

            market_slug,

        ))

        row = cur.fetchone()

        conn.close()

        if row:

            return dict(row)

        return None

    def has_position(

        self,

        market_slug

    ):

        return self.get_position(

            market_slug

        ) is not None

    def total_exposure(self):

        conn = self._connect()

        cur = conn.cursor()

        cur.execute("""

            SELECT

            COALESCE(SUM(usd_amount),0)

            FROM live_trades

            WHERE status='OPEN'

        """)

        exposure = cur.fetchone()[0]

        conn.close()

        return float(exposure)

    def total_shares(self):

        conn = self._connect()

        cur = conn.cursor()

        cur.execute("""

            SELECT

            COALESCE(SUM(shares),0)

            FROM live_trades

            WHERE status='OPEN'

        """)

        shares = cur.fetchone()[0]

        conn.close()

        return float(shares)

    def summary(self):

        return {

            "positions":

                len(

                    self.get_open_positions()

                ),

            "shares":

                self.total_shares(),

            "exposure":

                self.total_exposure()

        }