from datetime import datetime, timezone

from src.paper_trading.pnl import PnLCalculator

from src.paper_trading.settlement import SettlementEngine

from src.database.database import Database
from src.database.repository import Repository




class TradeManager:

    def __init__(self):

        self.db = Database()

        self.repo = Repository(self.db)

        self.settlement = SettlementEngine()

    def process(self):

        trades = self.repo.get_open_trades()

        print()

        print("=" * 60)

        print("OPEN TRADES")

        print("=" * 60)

        print()

        for trade in trades:

            winner = self.settlement.winner(

                trade[2]

            )

            if winner is None:

                print(

                    trade[2],

                    "Still Open"

                )

                continue

            result = PnLCalculator.calculate(

                trade[3],

                trade[7],

                winner

            )

            self.repo.close_trade(

                trade_id=trade[1],

                exit_time=datetime.now(

                    timezone.utc

                ).isoformat(),

                exit_price=result["exit_price"],

                btc_exit=None,

                pnl=result["pnl"],

                roi=result["roi"],

                result=winner

            )

            print(

                trade[2],

                "CLOSED",

                winner,

                result["pnl"]

            )

        