import sqlite3

from pathlib import Path

from config import DATABASE_PATH

from src.database.schema import (
    MARKETS_TABLE,
    MARKET_TICKS_TABLE,
    PAPER_TRADES_TABLE
)


class Database:

    def __init__(self):

        Path(DATABASE_PATH).parent.mkdir(exist_ok=True)

        self.conn = sqlite3.connect(DATABASE_PATH)

        self.cursor = self.conn.cursor()

        self.create_tables()

    def create_tables(self):

        self.cursor.execute(MARKETS_TABLE)

        self.cursor.execute(MARKET_TICKS_TABLE)

        self.cursor.execute(PAPER_TRADES_TABLE)

        self.conn.commit()

    def execute(self, query, values=()):

        self.cursor.execute(query, values)

        self.conn.commit()

    def fetchall(self, query, values=()):

        self.cursor.execute(query, values)

        return self.cursor.fetchall()

    def fetchone(self, query, values=()):

        self.cursor.execute(query, values)

        return self.cursor.fetchone()

    def close(self):

        self.conn.close()