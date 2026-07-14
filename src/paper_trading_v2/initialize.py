"""
Initialize V2 Database
"""

from src.paper_trading_v2.database import Database

from src.paper_trading_v2.schema import (

    PORTFOLIO_TABLE,

    POSITIONS_TABLE,

    PORTFOLIO_HISTORY_TABLE

)


class InitializeDatabase:

    def __init__(self):

        self.db = Database()

    def run(self):

        self.db.execute(PORTFOLIO_TABLE)

        self.db.execute(POSITIONS_TABLE)

        self.db.execute(PORTFOLIO_HISTORY_TABLE)

        print("V2 Database Ready")