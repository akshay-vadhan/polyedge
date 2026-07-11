from src.utils.logger import logger

from src.database.database import Database


def main():

    logger.info("Starting Polymarket Edge...")

    db = Database()

    logger.success("Database Connected")

    logger.success("Tables Created")

    db.close()

    logger.success("Ready")


if __name__ == "__main__":

    main()