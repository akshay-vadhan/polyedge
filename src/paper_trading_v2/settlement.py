"""
Settlement Engine V2
"""

from src.paper_trading.settlement import SettlementEngine


class Settlement:

    def __init__(self):

        self.engine = SettlementEngine()

    def resolve(

        self,

        position

    ):

        winner = self.engine.winner(

            position.market_slug

        )

        if winner is None:

            return None

        return winner