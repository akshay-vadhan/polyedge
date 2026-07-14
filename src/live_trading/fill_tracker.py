import time

from src.live_trading.client import LiveClient
from src.utils.logger import logger


class FillTracker:

    def __init__(self):

        self.client = LiveClient().get()

    def get_order(self, order_id):

        logger.info(
            f"Checking Order : {order_id}"
        )

        return self.client.get_order(order_id)

    def wait_until_finished(

        self,

        order_id,

        timeout=30,

        interval=1

    ):

        start = time.time()

        while True:

            order = self.get_order(order_id)

            status = order.get("status")

            logger.info(
                f"Order Status : {status}"
            )

            if status in (

                "MATCHED",

                "FILLED",

                "CANCELED"

            ):

                logger.success(
                    f"Final Status : {status}"
                )

                return order

            if time.time() - start > timeout:

                logger.warning(
                    "Order wait timeout."
                )

                return order

            time.sleep(interval)