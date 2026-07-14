from py_clob_client.clob_types import (
    BalanceAllowanceParams,
    AssetType
)

from src.live_trading.client import LiveClient


class LiveAccount:

    def __init__(self):

        self.client = LiveClient().get()

    def get_balance(self):

        params = BalanceAllowanceParams(

            asset_type=AssetType.COLLATERAL,

            signature_type=0

        )

        return self.client.get_balance_allowance(params)

    def print_info(self):

        balance = self.get_balance()

        print()

        print("=" * 60)

        print("POLYEDGE ACCOUNT")

        print("=" * 60)

        print()

        print("Wallet")

        print(self.client.get_address())

        print()

        print("USDC Balance")

        print(balance["balance"])

        print()

        print("Allowances")

        for token, value in balance["allowances"].items():

            print(token)

            print(value)

            print()