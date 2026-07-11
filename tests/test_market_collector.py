from pprint import pprint

from src.collectors.market_collector import MarketCollector

collector = MarketCollector()

tick = collector.collect()

pprint(tick)