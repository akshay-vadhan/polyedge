"""
Paper Trading V2 Test
"""

from src.paper_trading_v2.engine import PaperTradingEngineV2


engine = PaperTradingEngineV2()

trade = engine.buy(

    market_slug="btc-test",

    side="YES",

    entry_price=0.50,

    trade_amount=10

)

print()

print("="*60)

print("POSITION")

print("="*60)

print()

print(trade)

print()

print("="*60)

print("PORTFOLIO")

print("="*60)

print()

print(engine.portfolio_state())