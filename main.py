from src.api.gamma import GammaClient
from src.api.clob import ClobClient

gamma = GammaClient()
clob = ClobClient()

market = gamma.find_active_btc_market()

print("\nBTC MARKET")
print("--------------------------")
print(market)

print("\nUP ORDERBOOK")
print("--------------------------")

up = clob.get_best_bid_ask(market.up_token)

print(up)

print("\nDOWN ORDERBOOK")
print("--------------------------")

down = clob.get_best_bid_ask(market.down_token)

print(down)