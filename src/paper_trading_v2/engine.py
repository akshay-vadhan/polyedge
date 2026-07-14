from datetime import datetime
import uuid

from src.paper_trading_v2.models import Position

from src.paper_trading_v2.shares import SharesCalculator

from src.paper_trading_v2.portfolio import PortfolioManager

from src.paper_trading_v2.position import PositionManager

from src.paper_trading_v2.risk import RiskEngine


class PaperTradingEngineV2:

    def __init__(self):

        self.portfolio = PortfolioManager()

        self.positions = PositionManager()

        self.risk = RiskEngine()

    def buy(

        self,

        market_slug,

        side,

        entry_price,

        trade_amount

    ):

        ok, reason = self.risk.can_open_position(

            self.portfolio.snapshot(),

            trade_amount,

            self.positions.has_position()

        )

        if not ok:

            print(reason)

            return None

        calc = SharesCalculator.calculate(

            trade_amount,

            entry_price

        )

        self.portfolio.lock_cash(trade_amount)

        position = Position(

            position_id=str(uuid.uuid4()),

            market_slug=market_slug,

            side=side,

            entry_price=entry_price,

            shares=calc["shares"],

            trade_amount=trade_amount,

            current_price=entry_price,

            current_value=trade_amount,

            unrealized_pnl=0,

            max_payout=calc["max_payout"],

            max_profit=calc["max_profit"],

            max_loss=calc["max_loss"],

            status="OPEN"

        )

        self.positions.open(position)

        return position

    def current_position(self):

        return self.positions.current()

    def portfolio_state(self):

        return self.portfolio.snapshot()