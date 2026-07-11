class GammaAPIError(Exception):
    """Raised when Gamma API fails."""
    pass


class MarketNotFound(Exception):
    """Raised when BTC market not found."""
    pass