import json

from src.api.gamma import GammaClient

gamma = GammaClient()

market = gamma.find_active_btc_market()

print("\n========== MARKET OBJECT ==========\n")


print("\n===================================\n")