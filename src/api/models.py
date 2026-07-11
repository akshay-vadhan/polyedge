from dataclasses import dataclass
from typing import List


# ----------------------------------------------------
# Market Model
# ----------------------------------------------------

@dataclass
class Market:

    slug: str

    condition_id: str

    up_token: str

    down_token: str

    closed: bool

    enable_orderbook: bool


# ----------------------------------------------------
# OrderBook Models
# ----------------------------------------------------

@dataclass
class PriceLevel:

    price: float

    size: float


@dataclass
class OrderBook:

    token_id: str

    best_bid: float

    best_ask: float

    mid_price: float

    spread: float

    bid_volume: float

    ask_volume: float

    imbalance: float

    bids: List[PriceLevel]

    asks: List[PriceLevel]