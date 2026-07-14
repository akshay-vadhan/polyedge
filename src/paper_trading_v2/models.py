from dataclasses import dataclass


@dataclass
class Portfolio:

    balance: float

    available_cash: float

    locked_cash: float

    equity: float

    total_pnl: float


@dataclass
class Position:

    position_id: str

    market_slug: str

    side: str

    entry_price: float

    shares: float

    trade_amount: float

    current_price: float

    current_value: float

    unrealized_pnl: float

    max_payout: float

    max_profit: float

    max_loss: float

    status: str


@dataclass
class ClosedTrade:

    trade_id: str

    side: str

    entry_price: float

    exit_price: float

    shares: float

    payout: float

    pnl: float

    roi: float

    result: str