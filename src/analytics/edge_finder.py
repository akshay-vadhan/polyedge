from src.database.database import Database

from src.analytics.features import FeatureRow


class EdgeFinder:

    def __init__(self):

        self.db = Database()

    def latest_ticks(self, limit=300):

        query = """
        SELECT *
        FROM market_ticks
        ORDER BY id DESC
        LIMIT ?
        """

        return self.db.fetchall(query, (limit,))

    def average_yes_price(self):

        query = """
        SELECT AVG(yes_price)
        FROM market_ticks
        """

        return self.db.fetchone(query)[0]

    def average_liquidity(self):

        query = """
        SELECT AVG(liquidity)
        FROM market_ticks
        """

        return self.db.fetchone(query)[0]

    def average_volume(self):

        query = """
        SELECT AVG(volume)
        FROM market_ticks
        """

        return self.db.fetchone(query)[0]

    def average_yes_imbalance(self):

        query = """
        SELECT AVG(yes_imbalance)
        FROM market_ticks
        """

        return self.db.fetchone(query)[0]

    def build_features(self):

        rows = self.latest_ticks(1000)

        rows.reverse()

        features = []

        previous = None

        for row in rows:

            if previous is None:

                previous = row

                continue

            btc_change = row[3] - previous[3]

            yes_change = row[4] - previous[4]

            no_change = row[5] - previous[5]

            liquidity_change = row[10] - previous[10]

            volume_change = row[11] - previous[11]

            imbalance_change = row[13] - previous[13]

            

            features.append(

                FeatureRow(

                    timestamp=row[1],

                    btc_price=row[3],

                    yes_price=row[4],

                    no_price=row[5],

                    btc_change=btc_change,

                    yes_change=yes_change,

                    no_change=no_change,

                    liquidity_change=liquidity_change,

                    volume_change=volume_change,

                    imbalance_change=imbalance_change,

                    seconds_remaining=0

                )

            )
            previous = row

        return features