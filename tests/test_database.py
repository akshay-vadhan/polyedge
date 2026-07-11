from src.collectors.market_collector import MarketCollector
from src.database.database import Database
from src.database.repository import Repository

collector = MarketCollector()

db = Database()

repo = Repository(db)

tick = collector.collect()

repo.insert_market_tick(tick)

print("Saved Successfully")