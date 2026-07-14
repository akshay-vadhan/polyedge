from src.paper_trading_v2.models import Position


class PositionManager:

    def __init__(self):

        self.position = None

    def open(

        self,

        position

    ):

        self.position = position

    def current(self):

        return self.position

    def close(self):

        self.position = None

    def has_position(self):

        return self.position is not None