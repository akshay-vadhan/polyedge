from src.analytics.edge_finder import EdgeFinder

edge = EdgeFinder()

features = edge.build_features()

print(f"Features Found: {len(features)}")

for feature in features:
    print(feature)