from pprint import pprint

from src.paper_trading.engine import PaperTradingEngine

engine = PaperTradingEngine()

trade = engine.create_trade()

print()
print("=" * 60)
print("PAPER TRADE")
print("=" * 60)
print()

pprint(trade)