from pprint import pprint

from src.analytics.feature_engine import FeatureEngine

engine = FeatureEngine()

features = engine.build()

print()

print("=" * 60)

print("FEATURES")

print("=" * 60)

pprint(features)