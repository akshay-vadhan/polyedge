from src.paper_trading_v2.models import Portfolio

from src.paper_trading_v2.constants import INITIAL_BALANCE


class PortfolioManager:

    def __init__(self):

        self.portfolio = Portfolio(

            balance=INITIAL_BALANCE,

            available_cash=INITIAL_BALANCE,

            locked_cash=0,

            equity=INITIAL_BALANCE,

            total_pnl=0

        )

    def balance(self):

        return self.portfolio.balance

    def available(self):

        return self.portfolio.available_cash

    def lock_cash(

        self,

        amount

    ):

        self.portfolio.available_cash -= amount

        self.portfolio.locked_cash += amount

    def unlock_cash(

        self,

        amount

    ):

        self.portfolio.available_cash += amount

        self.portfolio.locked_cash -= amount

    def add_profit(

        self,

        pnl

    ):

        self.portfolio.balance += pnl

        self.portfolio.available_cash += pnl

        self.portfolio.total_pnl += pnl

        self.portfolio.equity = self.portfolio.balance

    def snapshot(self):

        return self.portfolio