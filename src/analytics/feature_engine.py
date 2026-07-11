from src.database.database import Database


class FeatureEngine:

    def __init__(self):

        self.db = Database()

    def latest_ticks(self, limit=2):

        query = """
        SELECT *
        FROM market_ticks
        ORDER BY id DESC
        LIMIT ?
        """

        rows = self.db.fetchall(
            query,
            (limit,)
        )

        rows.reverse()

        return rows

    def build(self):

        rows = self.latest_ticks()

        if len(rows) < 2:

            return None

        previous = rows[0]
        current = rows[1]

        features = {

            "btc_change":
                current[3] - previous[3],

            "yes_price_change":
                current[4] - previous[4],

            "no_price_change":
                current[5] - previous[5],

            "yes_bid_change":
                current[6] - previous[6],

            "yes_ask_change":
                current[7] - previous[7],

            "yes_mid_change":
                current[8] - previous[8],

            "yes_spread_change":
                current[9] - previous[9],

            "yes_bid_volume_change":
                current[10] - previous[10],

            "yes_ask_volume_change":
                current[11] - previous[11],

            "yes_imbalance_change":
                current[12] - previous[12],

            "no_bid_change":
                current[13] - previous[13],

            "no_ask_change":
                current[14] - previous[14],

            "no_mid_change":
                current[15] - previous[15],

            "no_spread_change":
                current[16] - previous[16],

            "no_bid_volume_change":
                current[17] - previous[17],

            "no_ask_volume_change":
                current[18] - previous[18],

            "no_imbalance_change":
                current[19] - previous[19],

            "last_trade_change":
                current[20] - previous[20],

            "liquidity_change":
                current[21] - previous[21],

            "volume_change":
                current[22] - previous[22],

            "one_hour_change_delta":
                current[23] - previous[23]

        }

        return features