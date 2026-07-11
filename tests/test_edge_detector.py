from src.strategy.edge_detector import EdgeDetector

edge = EdgeDetector()

signal = edge.detect()

print()

print("=" * 60)

print("EDGE SIGNAL")

print("=" * 60)

print()

from pprint import pprint

pprint(signal)