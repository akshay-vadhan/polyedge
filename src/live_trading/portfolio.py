import sqlite3


class PortfolioManager:

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

    def get_closed_positions(self):

        conn = self._connect()

        conn.row_factory = sqlite3.Row

        cur = conn.cursor()

        cur.execute("""

            SELECT *

            FROM live_trades

            WHERE status='CLOSED'

            ORDER BY closed_at DESC

        """)

        rows = cur.fetchall()

        conn.close()

        return [dict(r) for r in rows]

    def get_open_count(self):

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

    def get_portfolio_value(self):

        conn = self._connect()

        cur = conn.cursor()

        cur.execute("""

            SELECT

            COALESCE(SUM(usd_amount),0)

            FROM live_trades

            WHERE status='OPEN'

        """)

        value = cur.fetchone()[0]

        conn.close()

        return float(value)

    def get_realized_pnl(self):

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

        return float(pnl)

    def get_unrealized_pnl(self):

        """
        Placeholder.

        Future version will calculate
        using live market prices.
        """

        return 0.0

    def get_total_shares(self):

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

    def get_win_rate(self):

        conn = self._connect()

        cur = conn.cursor()

        cur.execute("""

            SELECT COUNT(*)

            FROM live_trades

            WHERE status='CLOSED'

        """)

        total = cur.fetchone()[0]

        if total == 0:

            conn.close()

            return 0.0

        cur.execute("""

            SELECT COUNT(*)

            FROM live_trades

            WHERE

            status='CLOSED'

            AND pnl > 0

        """)

        wins = cur.fetchone()[0]

        conn.close()

        return round(

            wins / total * 100,

            2

        )

    def summary(self):

        return {

            "open_positions":

                self.get_open_count(),

            "portfolio_value":

                self.get_portfolio_value(),

            "realized_pnl":

                self.get_realized_pnl(),

            "unrealized_pnl":

                self.get_unrealized_pnl(),

            "shares":

                self.get_total_shares(),

            "win_rate":

                self.get_win_rate()

        }