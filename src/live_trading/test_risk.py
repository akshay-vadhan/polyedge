from src.live_trading.risk import RiskManager


if __name__ == "__main__":

    risk = RiskManager()

    risk.validate(

        market_slug="btc-test",

        side="YES"

    )

    print()

    print("Risk Validation Passed")