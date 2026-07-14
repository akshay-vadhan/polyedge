"""
Share Calculator

Polymarket uses shares.

shares = amount / price
"""


class SharesCalculator:

    @staticmethod
    def calculate(

        trade_amount,

        entry_price

    ):

        shares = trade_amount / entry_price

        max_payout = shares

        max_profit = max_payout - trade_amount

        max_loss = trade_amount

        return {

            "shares": shares,

            "max_payout": max_payout,

            "max_profit": max_profit,

            "max_loss": max_loss

        }