from pprint import pprint

from src.live_trading.position_manager import (
    PositionManager
)


if __name__ == "__main__":

    manager = PositionManager()

    pprint(

        manager.summary()

    )