class GammaAPIError(Exception):
    """Raised when Gamma API fails."""
    pass


class MarketNotFound(Exception):
    """Raised when BTC market not found."""
    pass


class InsufficientBalanceError(Exception):
    """Raised when wallet balance is lower than required trade amount."""
    pass


class MarketClosedError(Exception):
    """Raised when market is not accepting orders."""
    pass


class OrderValidationError(Exception):
    """Raised when order validation fails."""
    pass


class RiskLimitExceeded(Exception):
    """Raised when risk limits are exceeded."""
    pass


class DuplicatePositionError(Exception):
    """Raised when a duplicate position already exists."""
    pass


class OrderSubmissionError(Exception):
    """Raised when order submission fails."""
    pass


class OrderRejectedError(Exception):
    """Raised when an order is rejected by the exchange."""
    pass