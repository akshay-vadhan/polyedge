from src.api.gamma import GammaClient

client = GammaClient()

market = client.find_active_btc_market()

print(market)