from dataclasses import dataclass


@dataclass
class Market:

    slug: str

    condition_id: str

    up_token: str

    down_token: str

    closed: bool

    enable_orderbook: bool