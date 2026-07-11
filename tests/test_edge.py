from src.analytics.edge_finder import EdgeFinder

edge = EdgeFinder()

print()

print("Average YES Price :", edge.average_yes_price())

print("Average Liquidity :", edge.average_liquidity())

print("Average Volume :", edge.average_volume())

print("Average YES Imbalance :", edge.average_yes_imbalance())