import requests

from src.utils.logger import logger


class GeoBlockChecker:

    URL = "https://polymarket.com/api/geoblock"

    def check(self):

        try:

            response = requests.get(

                self.URL,

                timeout=10

            )

            response.raise_for_status()

            data = response.json()

            return data

        except Exception as e:

            logger.error(f"Geo Check Failed : {e}")

            return None