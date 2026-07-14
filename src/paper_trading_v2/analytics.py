"""
Portfolio Analytics
"""

class Analytics:

    @staticmethod

    def position_summary(position):

        return {

            "Shares":

                round(position.shares, 2),

            "Current Value":

                round(position.current_value, 2),

            "PnL":

                round(position.unrealized_pnl, 2),

            "ROI":

                round(

                    (

                        position.unrealized_pnl

                        /

                        position.trade_amount

                    ) * 100,

                    2

                )

        }

    @staticmethod

    def portfolio_summary(

        portfolio

    ):

        return {

            "Balance":

                round(portfolio.balance, 2),

            "Cash":

                round(

                    portfolio.available_cash,

                    2

                ),

            "Locked":

                round(

                    portfolio.locked_cash,

                    2

                ),

            "Equity":

                round(

                    portfolio.equity,

                    2

                )

        }