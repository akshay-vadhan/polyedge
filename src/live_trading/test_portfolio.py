from pprint import pprint

from src.live_trading.portfolio import PortfolioManager


if __name__ == "__main__":

    portfolio = PortfolioManager()

    pprint(

        portfolio.summary()

    )