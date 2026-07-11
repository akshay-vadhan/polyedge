from dataclasses import dataclass

@dataclass
class FeatureRow:

    timestamp: str

    btc_price: float

    yes_price: float

    no_price: float

    btc_change: float

    yes_change: float

    no_change: float

    liquidity_change: float

    volume_change: float

    imbalance_change: float

    seconds_remaining: int