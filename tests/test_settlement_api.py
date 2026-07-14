import json

from src.api.gamma import GammaClient

client = GammaClient()

slug = input("Market Slug : ").strip()

event = client.get_event_by_slug(slug)

print()

print("=" * 80)

print(json.dumps(event, indent=2))

print("=" * 80)