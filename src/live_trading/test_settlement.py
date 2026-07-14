from src.live_trading.settlement import SettlementEngine

engine = SettlementEngine()

engine.settle_trade(

    input("Order ID : ")

)