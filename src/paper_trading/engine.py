from datetime import datetime, timezone

from src.strategy.edge_detector import EdgeDetector

from src.database.database import Database
from src.database.repository import Repository

from src.utils.logger import logger

MIN_CONFIDENCE = 80


class PaperTradingEngine:

    def __init__(self):

        self.detector = EdgeDetector()

        self.db = Database()

        self.repo = Repository(self.db)

    def create_trade(self):

        signal = self.detector.detect()

        if signal is None:
            return None

        if signal.signal == "NO_TRADE":
            return None

        if self.repo.trade_exists(signal.market_slug):

            logger.info(

                f"Trade already exists for {signal.market_slug}"

            )

            return None

        if signal.confidence < MIN_CONFIDENCE:

            logger.info(

                f"Low confidence {signal.confidence}"

            )

            return None

        if signal.signal == "BUY_YES":
            entry_price = signal.yes_price
            side = "YES"

        else:
            entry_price = signal.no_price
            side = "NO"

        trade = {

            "trade_id": datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S"),

            "market_slug": signal.market_slug,

            "side": side,

            "status": "OPEN",

            "entry_time": signal.timestamp,

            "exit_time": None,

            "entry_price": entry_price,

            "exit_price": None,

            "btc_entry": signal.btc_price,

            "btc_exit": None,

            "confidence": signal.confidence,

            "score": signal.score,

            "pnl": 0,

            "roi": 0,

            "result": "",

            "reason": ", ".join(signal.reasons)

        }

        self.repo.insert_trade(trade)

        return trade