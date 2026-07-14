from dataclasses import dataclass
from typing import List


# ---------------------------------------------------------
# Orderbook Models
# ---------------------------------------------------------

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


# ---------------------------------------------------------
# Market Model
# ---------------------------------------------------------

@dataclass
class Market:

    slug: str
    condition_id: str

    up_token: str
    down_token: str

    tick_size: str
    neg_risk: bool
    min_order_size: float
    end_time: str
    accepting_orders: bool

    closed: bool
    enable_orderbook: bool


    # Gamma Data

    yes_price: float
    no_price: float

    best_bid: float
    best_ask: float

    last_trade: float

    spread: float

    liquidity: float

    volume: float

    one_hour_change: float