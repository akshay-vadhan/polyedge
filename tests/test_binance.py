from src.api.binance import BinanceClient

client = BinanceClient()

print()

print(client.get_price())