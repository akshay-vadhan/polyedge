"""
Risk Engine
"""


class RiskEngine:

    def __init__(self):

        self.max_open_positions = 1

        self.max_trade_size = 10

    def can_open_position(

        self,

        portfolio,

        trade_size,

        has_position

    ):

        if has_position:

            return False, "Already holding a position"

        if portfolio.available_cash < trade_size:

            return False, "Insufficient balance"

        if trade_size > self.max_trade_size:

            return False, "Trade size too large"

        return True, "OK"