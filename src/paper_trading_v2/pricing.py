"""
Live Position Pricing Engine
"""

from dataclasses import replace


class PricingEngine:

    @staticmethod
    def update(position, current_price):

        current_value = position.shares * current_price

        unrealized_pnl = current_value - position.trade_amount

        roi = (unrealized_pnl / position.trade_amount) * 100

        return replace(

            position,

            current_price=current_price,

            current_value=current_value,

            unrealized_pnl=unrealized_pnl

        ), roi