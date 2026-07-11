from dataclasses import dataclass

from src.database.database import Database

from src.analytics.feature_engine import FeatureEngine


@dataclass
class Signal:

    signal: str

    confidence: int

    score: int

    reasons: list

    market_slug: str

    yes_price: float

    no_price: float

    btc_price: float

    timestamp: str

class EdgeDetector:

    def __init__(self):
        self.engine = FeatureEngine()
        self.db = Database()

    def detect(self):

        f = self.engine.build()

        row = self.db.fetchone("""

        SELECT *

        FROM market_ticks

        ORDER BY id DESC

        LIMIT 1

        """)

        if f is None:
            return None

        score = 0
        reasons = []

        # ------------------------------------------------
        # BTC Direction (Weight = 3)
        # ------------------------------------------------

        if f["btc_change"] > 0:
            score += 3
            reasons.append("BTC Rising")

        elif f["btc_change"] < 0:
            score -= 3
            reasons.append("BTC Falling")

        # ------------------------------------------------
        # YES Price
        # ------------------------------------------------

        if f["yes_price_change"] > 0:
            score += 2
            reasons.append("YES Price Rising")

        elif f["yes_price_change"] < 0:
            score -= 2
            reasons.append("YES Price Falling")

        # ------------------------------------------------
        # NO Price
        # ------------------------------------------------

        if f["no_price_change"] > 0:
            score -= 2
            reasons.append("NO Price Rising")

        elif f["no_price_change"] < 0:
            score += 2
            reasons.append("NO Price Falling")

        # ------------------------------------------------
        # YES Imbalance
        # ------------------------------------------------

        if f["yes_imbalance_change"] > 0:
            score += 3
            reasons.append("YES Imbalance Increasing")

        elif f["yes_imbalance_change"] < 0:
            score -= 3
            reasons.append("YES Imbalance Falling")

        # ------------------------------------------------
        # NO Imbalance
        # ------------------------------------------------

        if f["no_imbalance_change"] > 0:
            score -= 3
            reasons.append("NO Imbalance Increasing")

        elif f["no_imbalance_change"] < 0:
            score += 3
            reasons.append("NO Imbalance Falling")

        # ------------------------------------------------
        # YES Bid Volume
        # ------------------------------------------------

        if f["yes_bid_volume_change"] > 0:
            score += 2
            reasons.append("YES Bid Volume Up")

        # ------------------------------------------------
        # NO Bid Volume
        # ------------------------------------------------

        if f["no_bid_volume_change"] > 0:
            score -= 2
            reasons.append("NO Bid Volume Up")

        # ------------------------------------------------
        # Liquidity
        # ------------------------------------------------

        if f["liquidity_change"] > 0:
            score += 1
            reasons.append("Liquidity Increasing")

        elif f["liquidity_change"] < 0:
            score -= 1
            reasons.append("Liquidity Decreasing")

        # ------------------------------------------------
        # Market Volume
        # ------------------------------------------------

        if f["volume_change"] > 0:
            score += 1
            reasons.append("Market Volume Increasing")

        elif f["volume_change"] < 0:
            score -= 1
            reasons.append("Market Volume Decreasing")

        # ------------------------------------------------
        # Last Trade
        # ------------------------------------------------

        if f["last_trade_change"] > 0:
            score += 1
            reasons.append("Last Trade Up")

        elif f["last_trade_change"] < 0:
            score -= 1
            reasons.append("Last Trade Down")

        # ------------------------------------------------
        # Confidence
        # ------------------------------------------------

        confidence = min(abs(score) * 8, 100)

        # ------------------------------------------------
        # Final Decision
        # ------------------------------------------------

        if score >= 8:
            signal = "BUY_YES"

        elif score <= -8:
            signal = "BUY_NO"

        else:
            signal = "NO_TRADE"

        return Signal(

            signal=signal,

            confidence=confidence,

            score=score,

            reasons=reasons,

            market_slug=row[2],

            btc_price=row[3],

            yes_price=row[4],

            no_price=row[5],

            timestamp=row[1]

        )