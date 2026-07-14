import requests


class MarketLookup:

    GAMMA_URL = "https://gamma-api.polymarket.com"

    def get_market(self, slug: str):

        url = f"{self.GAMMA_URL}/markets"

        r = requests.get(

            url,

            params={

                "slug": slug

            },

            timeout=15

        )

        r.raise_for_status()

        data = r.json()

        if not data:

            raise Exception(

                f"Market not found: {slug}"

            )

        return data[0]

    def get_token_id(self, slug):

        market = self.get_market(slug)

        return market["clobTokenIds"][0]

    def get_tick_size(self, slug):

        market = self.get_market(slug)

        return market["orderPriceMinTickSize"]

    def get_neg_risk(self, slug):

        market = self.get_market(slug)

        return market.get(

            "enableNegRisk",

            False

        )

    def get_yes_token(self, slug):

        market = self.get_market(slug)

        return market["clobTokenIds"][0]

    def get_no_token(self, slug):

        market = self.get_market(slug)

        return market["clobTokenIds"][1]

    def info(self, slug):

        market = self.get_market(slug)

        print()

        print("=" * 60)

        print("MARKET")

        print("=" * 60)

        print()

        print("Question")

        print(market["question"])

        print()

        print("Slug")

        print(market["slug"])

        print()

        print("YES Token")

        print(self.get_yes_token(slug))

        print()

        print("NO Token")

        print(self.get_no_token(slug))

        print()

        print("Tick Size")

        print(self.get_tick_size(slug))

        print()

        print("Neg Risk")

        print(self.get_neg_risk(slug))