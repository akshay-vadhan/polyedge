import os
from dotenv import load_dotenv

from py_clob_client.client import ClobClient
from py_clob_client.clob_types import BalanceAllowanceParams, AssetType

load_dotenv()

client = ClobClient(
    host="https://clob.polymarket.com",
    chain_id=137,
    key=os.getenv("PRIVATE_KEY"),
    signature_type=2,
    funder="0x5fD85C70Bf902868727B183aCc7370C98f0f4Cb0"
)

client.set_api_creds(
    client.create_or_derive_api_creds()
)

params = BalanceAllowanceParams(
    asset_type=AssetType.COLLATERAL
)

print(client.get_balance_allowance(params))