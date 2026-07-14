"""
Position Manager
"""

from src.paper_trading_v2.pricing import PricingEngine

from src.paper_trading_v2.analytics import Analytics

from src.paper_trading_v2.settlement import Settlement


class PositionManager:

    def __init__(self):

        self.settlement = Settlement()

    def update(

        self,

        position,

        current_price

    ):

        position, roi = PricingEngine.update(

            position,

            current_price

        )

        summary = Analytics.position_summary(

            position

        )

        winner = self.settlement.resolve(

            position

        )

        return {

            "position": position,

            "roi": roi,

            "summary": summary,

            "winner": winner

        }