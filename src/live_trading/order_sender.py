from py_clob_client.clob_types import OrderType

from src.live_trading.client import LiveClient
from src.utils.logger import logger
from src.api.exceptions import OrderSubmissionError


class OrderSender:

    def __init__(self):

        self.client = LiveClient().get()

    def send(

        self,

        signed_order,

        order_type=OrderType.GTC,

        post_only=False

    ):

        try:

            logger.info("Submitting order...")

            response = self.client.post_order(

                signed_order,

                orderType=order_type,

                post_only=post_only

            )

            logger.success("Order submitted successfully")

            return response

        except Exception as e:

            logger.error(f"Order submission failed : {e}")

            raise OrderSubmissionError(str(e))