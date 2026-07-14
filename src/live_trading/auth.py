from py_clob_client.client import ClobClient

from src.live_trading.config import *


class LiveAuthenticator:

    def __init__(self):

        # Level 1 Client

        self.client = ClobClient(

            host=HOST,

            chain_id=CHAIN_ID,

            key=PRIVATE_KEY,

            signature_type=0,

            funder=WALLET_ADDRESS

        )

    def authenticate(self):

        print()

        print("=" * 60)

        print("POLYEDGE LIVE AUTH")

        print("=" * 60)

        print()

        print("Wallet")

        print(self.client.get_address())

        print()

        print("Creating L2 Credentials...")

        creds = self.client.create_or_derive_api_creds()

        self.client.set_api_creds(creds)

        print("✓ L2 Authentication Success")

        return self.client