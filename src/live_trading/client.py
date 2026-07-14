from src.live_trading.auth import LiveAuthenticator


class LiveClient:

    _instance = None
    _client = None

    def __new__(cls):

        if cls._instance is None:

            cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self):

        if LiveClient._client is None:

            print("Initializing Live Client...")

            LiveClient._client = (

                LiveAuthenticator()

                .authenticate()

            )

    def get(self):

        return LiveClient._client